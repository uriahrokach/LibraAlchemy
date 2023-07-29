import requests
import pytest

ENDPOINT = "http://127.0.0.1:5000"


def test_get_materials():
    res = requests.get(f"{ENDPOINT}/materials")
    assert list(sorted(res.json())) == list(
        sorted(
            [
                "לוטוס דם",
                "דרדר דרקון",
                "פטריות מעמקים",
                "תפרחת השעווה",
                "שורש אלף אצילי",
                "לילית שחורה",
                "קשקשי לטאת ענק",
            ]
        )
    )


def test_get_technics():
    res = requests.get(f"{ENDPOINT}/technics")
    assert sorted(res.json()) == sorted(["בישול", "ייבוש וכתישה", "התססה", "חליטה"])
