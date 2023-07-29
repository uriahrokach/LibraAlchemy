import requests
import pytest

from backend.tests.app.api.response_models.effects import STING_EFFECT, PARANOIA_EFFECT

ENDPOINT = "http://127.0.0.1:5000"


@pytest.mark.parametrize(
    "names,expected", [("צורב", [STING_EFFECT]), ("פראנויה", [PARANOIA_EFFECT])]
)
def test_get_effect_by_name_success(names, expected):
    res = requests.get(f"{ENDPOINT}/effect", json={"name": names})
    assert res.status_code == 200 and res.json() == expected


@pytest.mark.parametrize(
    "names",
    [
        "בלה בלה",
        "פסטן פסטנינו",
        1,
    ],
)
def test_get_effect_by_name_not_found(names):
    res = requests.get(f"{ENDPOINT}/effect", json={"name": names})
    assert res.status_code == 404


@pytest.mark.parametrize("request_json", [{"name": ["blabla"]}, {}, {"a": "b"}])
def test_get_effect_by_name_invalid(request_json):
    res = requests.get(f"{ENDPOINT}/effect", json=request_json)
    assert res.status_code == 422
