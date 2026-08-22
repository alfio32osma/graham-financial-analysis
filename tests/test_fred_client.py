import pytest
from unittest.mock import patch
from src.fred_client import get_yields_AAA

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
    with patch("src.fred_client.requests.get") as mock_get:
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
    with patch("src.fred_client.requests.get") as mock_get:
        mock_get.return_value.json.return_value = false_data

        with pytest.raises(ValueError, match="Is not a number"):
            get_yields_AAA()
