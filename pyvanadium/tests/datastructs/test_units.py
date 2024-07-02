import pytest

import pyvanadium.src.datastructs.composition as composition
from pyvanadium.src.datastructs.composition import units


def test_manual_convert_wppm_to_wt_percent():
    my_quantity = 461.0 * units.wppm
    assert (my_quantity.to(units.wt_pct)).magnitude == pytest.approx(0.0461)

    my_other_quantity = 0.35 * units.wt_percent
    assert (my_other_quantity.to(units.wppm)).magnitude == pytest.approx(3500)


@pytest.mark.parametrize(
    "test_input,expected",
    [(461.0, 0.0461), (1011.0, 0.1011), (742.0, 0.0742), (35.0, 0.0035)],
)
def test_wppm_to_wt_percent(test_input, expected):
    my_quantity = test_input * units.wppm
    assert (my_quantity.to(units.wt_pct)).magnitude == pytest.approx(expected)

    with pytest.raises(Exception):
        assert (expected * units.wppm).magnitude == test_input


@pytest.mark.parametrize(
    "test_input,expected",
    [(0.0461, 461.0), (0.1011, 1011.0), (0.0742, 742.0), (0.0035, 35)],
)
def test_wt_percent_to_wppm(test_input, expected):
    my_quantity = test_input * units.wt_percent
    assert (my_quantity.to(units.wppm)).magnitude == pytest.approx(expected)

    with pytest.raises(Exception):
        assert (expected * units.wppm).magnitude == test_input
