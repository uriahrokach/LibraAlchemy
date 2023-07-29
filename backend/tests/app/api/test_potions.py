import requests
import pytest

from backend.tests.app.api.response_models.potions import (
    COUNTER_POTION,
    LAST_WATCH_POTION,
    WEAKNESS_POISON_POTION,
    TRUTH_SYRUP_POTION,
    HEALTH_POTION,
    FAILED_POTION_VALIDATE_MATERIAL,
    FAILED_POTION_VALIDATE_TECHNIC,
    FAILED_POTION_TO_HIGH_MATERIAL,
    FAILED_POTION_TO_LOW_MATERIAL,
)

ENDPOINT = "http://127.0.0.1:5000"


@pytest.mark.parametrize(
    "request_json",
    [
        COUNTER_POTION,
        LAST_WATCH_POTION,
        WEAKNESS_POISON_POTION,
        TRUTH_SYRUP_POTION,
        HEALTH_POTION,
    ],
)
def test_create_potion(request_json):
    create_res = requests.put(f"{ENDPOINT}/potion", json=request_json)
    assert create_res.status_code == 201


@pytest.mark.parametrize(
    "request_json",
    [
        COUNTER_POTION,
        LAST_WATCH_POTION,
    ],
)
def test_failed_create_already_exists_potion(request_json):
    create_res = requests.put(f"{ENDPOINT}/potion", json=request_json)
    assert create_res.status_code == 400


@pytest.mark.parametrize(
    "request_json,expected_details",
    [
        (FAILED_POTION_VALIDATE_MATERIAL, "Material fail is not a valid material"),
        (FAILED_POTION_VALIDATE_TECHNIC, "Technic fail is not a valid technic"),
    ],
)
def test_validate_failed_create_potion(request_json, expected_details):
    res = requests.put(f"{ENDPOINT}/potion", json=request_json)
    assert res.status_code == 400 and res.json()["detail"] == expected_details


@pytest.mark.parametrize(
    "request_json",
    [
        FAILED_POTION_TO_HIGH_MATERIAL,
        FAILED_POTION_TO_LOW_MATERIAL,
    ],
)
def test_material_number_failed_create_potion(request_json):
    res = requests.put(f"{ENDPOINT}/potion", json=request_json)
    assert (
        res.status_code == 400
        and res.json()["detail"] == f"Number of materials must be between 3 and 6"
    )


@pytest.mark.parametrize(
    "name,expected_json",
    [
        ("נוגדן רעלים", COUNTER_POTION),
        ("אשמורת אחרונה", LAST_WATCH_POTION),
        ("רעל חולשה", WEAKNESS_POISON_POTION),
        ("סם אמת", TRUTH_SYRUP_POTION),
        ("מרקחת בריאות", HEALTH_POTION),
    ],
)
def test_get_potion(name, expected_json):
    res = requests.get(f"{ENDPOINT}/potion/{name}")
    assert (
        res.status_code == 200
        and res.json()["description"] == expected_json["description"]
    )


@pytest.mark.parametrize("name", ["fake"])
def test_failed_not_found_get_potion(name):
    res = requests.get(f"{ENDPOINT}/potion/{name}")
    assert res.status_code == 404


@pytest.mark.parametrize(
    "regex,expected_potions",
    [
        ("רעל", [COUNTER_POTION, WEAKNESS_POISON_POTION]),
        ("א", [LAST_WATCH_POTION, TRUTH_SYRUP_POTION, HEALTH_POTION]),
        (
            "ו",
            [COUNTER_POTION, LAST_WATCH_POTION, WEAKNESS_POISON_POTION, HEALTH_POTION],
        ),
        ("fake", []),
        (
            "",
            [
                COUNTER_POTION,
                LAST_WATCH_POTION,
                WEAKNESS_POISON_POTION,
                TRUTH_SYRUP_POTION,
                HEALTH_POTION,
            ],
        ),
    ],
)
def test_regex_potion(regex, expected_potions):
    res = requests.get(
        f"{ENDPOINT}/potion?regex={regex}",
    )
    assert sorted([potion["name"] for potion in res.json()]) == sorted(
        [potion["name"] for potion in expected_potions]
    )


def test_regex_potion_no_param():
    res = requests.get(
        f"{ENDPOINT}/potion",
    )
    print(res.json())
    assert sorted([potion["name"] for potion in res.json()]) == sorted(
        [
            potion["name"]
            for potion in [
                COUNTER_POTION,
                LAST_WATCH_POTION,
                WEAKNESS_POISON_POTION,
                TRUTH_SYRUP_POTION,
                HEALTH_POTION,
            ]
        ]
    )


@pytest.mark.parametrize(
    "name,request_json",
    [
        ("נוגדן רעלים", COUNTER_POTION),
        ("אשמורת אחרונה", LAST_WATCH_POTION),
        ("רעל חולשה", WEAKNESS_POISON_POTION),
        ("סם אמת", TRUTH_SYRUP_POTION),
        ("מרקחת בריאות", HEALTH_POTION),
    ],
)
def test_delete_potion(name, request_json):
    res = requests.delete(f"{ENDPOINT}/potion/{name}")
    assert res.status_code == 200


@pytest.mark.parametrize("name", ["fake"])
def test_failed_delete_potion_not_found(name):
    res = requests.delete(f"{ENDPOINT}/potion/{name}")
    assert res.status_code == 404
