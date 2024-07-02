from typing import Annotated, Dict, List, Literal, Optional, Tuple

import attrs
import pinttr.converters
import pinttrs
import pydantic as pdt

from pyvanadium.src.datastructs.unit_registry import units

pinttrs.set_unit_registry(units)


@attrs.define
class Composition:
    composition: Dict
    alloying_elements: Optional[List[str]] = None
    impurities: Optional[List[str]] = None

    def vanadium_percentage(self):
        if "V" not in self.composition.keys():
            balance = 100.0 * units.wt_percent
            constituents = 0.0 * units.wt_percent
            for key, value in self.composition.items():
                constituents = constituents + value.to(units.wt_percent)
                balance = balance - value.to(units.wt_percent)

            self.composition["V"] = balance
        return self.composition["V"]

    def wt_percent_components(self, elements_list: List):
        if "V" not in self.composition.keys():
            self.vanadium_percentage()  # make sure composition dict has been
            # updated to include computed vanadium balance
        total = 0.0 * units.wt_percent
        for elem in elements_list:
            val = self.composition[elem]
            total = total + val.to(units.wt_percent)
        return total

    def total_impurity_wt_percent(self):
        try:
            return self.wt_percent_components(self.impurities)
        except TypeError:
            raise ValueError(
                "Impurity list was not passed in when "
                "initializing this Composition instance. Cannot "
                "compute total impurity content without "
                "list of impurities."
            )


@attrs.define
class Heat:
    id: str
    composition: Composition


@attrs.define
class Sample:
    composition: dict
