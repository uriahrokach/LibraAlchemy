import requests
import pytest
from contextlib import contextmanager
from typing import List

from backend.tests.app.api.response_models.potions import (
    COUNTER_POTION,
    LAST_WATCH_POTION,
    WEAKNESS_POISON_POTION,
    TRUTH_SYRUP_POTION,
    HEALTH_POTION,
)

ENDPOINT = "http://127.0.0.1:5000"


@contextmanager
def potion_sandbox(potions: List[dict]):
    for potion in potions:
        requests.put(f"{ENDPOINT}/potion", json=potion)
    yield
    for potion in potions:
        requests.delete(f'{ENDPOINT}/potion/{potion["name"]}')


@pytest.mark.parametrize(
    "materials,technic,expected",
    [
        (["לילית שחורה", "קשקשי לטאת ענק", "דרדר דרקון"], "בישול", [COUNTER_POTION]),
        (
            ["לילית שחורה", "פטריות מעמקים", "שורש אלף אצילי", "דרדר דרקון"],
            "התססה",
            [TRUTH_SYRUP_POTION],
        ),
        (
            ["לילית שחורה", "פטריות מעמקים", "שורש אלף אצילי", "דרדר דרקון"],
            "ייבוש וכתישה",
            [],
        ),
        (
            ["לילית שחורה", "קשקשי לטאת ענק", "דרדר דרקון", "לוטוס דם"],
            "בישול",
            [COUNTER_POTION],
        ),
        (
            ["לילית שחורה", "קשקשי לטאת ענק", "דרדר דרקון", "לוטוס דם", "תפרחת השעווה"],
            "בישול",
            [COUNTER_POTION, HEALTH_POTION],
        ),
    ],
)
def test_brew_potion(materials, technic, expected):
    with potion_sandbox(
        [
            COUNTER_POTION,
            LAST_WATCH_POTION,
            WEAKNESS_POISON_POTION,
            TRUTH_SYRUP_POTION,
            HEALTH_POTION,
        ]
    ):
        res = requests.post(
            f"{ENDPOINT}/brew", json={"materials": materials, "technic": technic}
        )
        print(res.json())
    assert sorted([potion["name"] for potion in res.json()]) == sorted(
        [potion["name"] for potion in expected]
    )


@pytest.mark.parametrize(
    "materials,technic",
    [
        (["קשקשי לטאת ענק", "דרדר דרקון"], "בישול"),
        (
            [
                "לילית שחורה",
                "שורש אלף אצילי",
                "קשקשי לטאת ענק",
                "לוטוס דם",
                "דרדר דרקון",
                "פטריות מעמקים",
                "תפרחת השעווה",
            ],
            "התססה",
        ),
    ],
)
def test_failed_material_number_brew(materials, technic):
    res = requests.post(
        f"{ENDPOINT}/brew", json={"materials": materials, "technic": technic}
    )
    assert (
        res.status_code == 400
        and res.json()["detail"] == f"Number of materials must be between 3 and 6"
    )


@pytest.mark.parametrize(
    "materials,technic,expected",
    [
        (
            ["לילית שחורה", "שורש אלף אצילי", "fail", "תפרחת השעווה"],
            "בישול",
            "Material fail is not a valid material",
        ),
        (
            ["לילית שחורה", "שורש אלף אצילי", "קשקשי לטאת ענק", "תפרחת השעווה"],
            "fail",
            "Technic fail is not a valid technic",
        ),
    ],
)
def test_failed_validate_ingredients_brew(materials, technic, expected):
    res = requests.post(
        f"{ENDPOINT}/brew", json={"materials": materials, "technic": technic}
    )
    assert res.status_code == 400 and res.json()["detail"] == expected
