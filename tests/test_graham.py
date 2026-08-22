import pytest
from src.graham_valuation import get_intrinsic_value

def test_get_intrinsic_value():
    assert get_intrinsic_value(0.10, 0.03, 3.97, 5.76) == pytest.approx(0.80, rel=0.01)
    assert get_intrinsic_value(0.35, 0.01, 3.97, 5.76) == pytest.approx(2.78, rel=0.01)
    assert get_intrinsic_value(1.00, 0.01, 3.97, 5.76) == pytest.approx(7.95, rel=0.01)
    with pytest.raises(ValueError):
        get_intrinsic_value(0.25, 0.02, 0, 5.76)
    with pytest.raises(ValueError):
        get_intrinsic_value(0.30, 0.03, 3.97, 0)