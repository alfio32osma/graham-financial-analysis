import pytest
from src.validators import get_number

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