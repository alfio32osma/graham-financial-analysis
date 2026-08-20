import pytest
from unittest.mock import patch
from project import get_number, get_yields_AAA, get_intrinsic_value

def test_get_intrinsic_value():
    assert get_intrinsic_value(0.10, 0.03, 3.97, 5.76) == pytest.approx(0.80, rel=0.01)
    assert get_intrinsic_value(0.35, 0.01, 3.97, 5.76) == pytest.approx(2.78, rel=0.01)
    assert get_intrinsic_value(1.00, 0.01, 3.97, 5.76) == pytest.approx(7.95, rel=0.01)
    with pytest.raises(ValueError):
        get_intrinsic_value(0.25, 0.02, 0, 5.76)
    with pytest.raises(ValueError):
        get_intrinsic_value(0.30, 0.03, 3.97, 0)


def test_get_number():
    assert get_number("120") == 120.0
    assert get_number("0.25") == 0.25
    assert get_number("1") == 1.0
    assert get_number("125.25") == 125.25
    assert get_number("1000000") == 1000000
    with pytest.raises(ValueError):
        get_number("Alfio Osma")
    with pytest.raises(ValueError):
        get_number("-12")

def test_get_yields_AAA():
    false_data = {
        "observations": [
            {"value": "10"},
            {"value": "5"},
            {"value": "ant"},
            {"value": "0"},
            {"value": "5"}
        ]
    }
    with patch("project.requests.get") as mock_get:
        mock_get.return_value.json.return_value = false_data
        result = get_yields_AAA()

        assert isinstance(result, list)
        assert len(result) == 2

        assert result[0] == 5
        assert result[1] == 6.67

def test_get_yields_AAA_error():
    false_data = {
        "observations": [
            {"value": "10"},
            {"Value": "5"},
            {"value": "ant"}
            ]
        }
    with patch("project.requests.get") as mock_get:
        mock_get.return_value.json.return_value = false_data

        with pytest.raises(ValueError, match="Is not a number"):
            get_yields_AAA()

