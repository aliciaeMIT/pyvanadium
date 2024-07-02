import pytest

from pyvanadium.src.datastructs.composition import Composition, units


@pytest.mark.parametrize(
    "cr,ti,si," "exp_v,exp_impurity," "exp_alloying",
    [
        (3.8, 3.9, 783, 92.1742, 0.1258, 7.7),
        (3.8, 3.9, 50, 92.2475, 0.0525, 7.7),
        (3.8, 3.9, 3000, 91.9525, 0.3475, 7.7),
        (4.1, 4.2, 1000, 91.5525, 0.1475, 8.3),
    ],
)
def test_composition(cr, ti, si, exp_v, exp_impurity, exp_alloying):
    alloy_comp = {
        "Cr": cr * units.wt_percent,
        "Ti": ti * units.wt_percent,
        "O": 310 * units.wppm,
        "N": 85 * units.wppm,
        "C": 80 * units.wppm,
        "Si": si * units.wppm,
    }

    alloying_elems = ["V", "Cr", "Ti"]
    impure = ["O", "N", "C", "Si"]

    my_comp = Composition(
        composition=alloy_comp, alloying_elements=alloying_elems, impurities=impure
    )

    assert my_comp.vanadium_percentage().magnitude == pytest.approx(exp_v)

    assert my_comp.wt_percent_components(impure).magnitude == pytest.approx(
        exp_impurity
    )

    assert my_comp.wt_percent_components(["Cr", "Ti"]).magnitude == pytest.approx(
        exp_alloying
    )

    everything = alloying_elems + impure

    assert my_comp.wt_percent_components(everything).magnitude == pytest.approx(100)

    assert my_comp.total_impurity_wt_percent().magnitude == pytest.approx(exp_impurity)


def test_heat():
    assert True
