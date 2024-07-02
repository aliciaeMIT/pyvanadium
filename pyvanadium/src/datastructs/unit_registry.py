import attrs
import pinttrs
from pint import UnitRegistry

units = UnitRegistry()
print("Unit registry initialized")

units.define("displacements_per_atom = [dose] = 1 = dpa")
units.define("neutron_dpa = 1*dpa = dpa_n")
units.define("ion_dpa = 1*dpa = dpa_i")

units.define("weight_percent = 1*percent = wt_pct = wt_percent = wpct")
units.define("weight_parts_per_million = 1*ppm = wppm")


def get_unit_registry():
    return units


def get_new_unit_registry():
    reg = UnitRegistry()
    print("Unit registry initialized")

    # register dpa as a custom unit
    reg.define("displacements_per_atom = [dose] = 1 = dpa")
    reg.define("neutron_dpa = 1*dpa = dpa_n")
    reg.define("ion_dpa = 1*dpa = dpa_i")

    reg.define("weight_percent = 1*percent = wt_pct = wt_percent = wpct")
    reg.define("weight_parts_per_million = 1*ppm = wppm")

    return reg
