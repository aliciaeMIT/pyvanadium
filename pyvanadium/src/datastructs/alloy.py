from typing import List

# , Optional
import pydantic as pdt
import pymatgen.core as pg


class Alloy(pdt.BaseModel):
    elements: List[pg.Element]
    composition: pg.Composition
    weight_percents: dict


class AlloyBuilder:
    pass


class AlloyOld:
    def __init__(self, weight_dict: dict):
        self._wt_fracs = weight_dict
        self._generate_element_instances()
        self._generate_composition()

    def _validate_weight_dict(self):
        """
        TODO: ensure keys are valid element names in format for pymatgen
        TODO: validate that values are numbers
        TODO: validate that percents add to 100
        :return:
        """
        if bool(self._wt_fracs):
            raise ValueError(
                "Weight percent dictionary must include at least 1 "
                "element:weight to initialize new Alloy instance."
            )

    def _generate_element_instances(self):
        try:
            self._elements = []
            for key in self._wt_fracs.keys():
                self._elements.append(pg.Element(key))
        except AttributeError as e:
            raise ValueError(
                "Weight percent dictionary must be provided to initialize "
                "new Alloy instance (not a list)."
            ) from e

    def _generate_composition(self):
        try:
            self._composition = pg.Composition.from_weight_dict(self._wt_fracs)
        except ZeroDivisionError as e:
            raise ValueError(
                "Cannot generate Alloy that includes an element "
                "with zero weight percent... check weight percent dictionary"
            ) from e


if __name__ == "__main__":
    elem_vanadium = pg.Element("V")
    elem_cr = pg.Element("Cr")
    elem_ti = pg.Element("Ti")

    wt_frac_cr = 4.0
    wt_frac_ti = 4.0
    wt_frac_v = 100 - wt_frac_cr - wt_frac_ti

    weights_v44 = {
        "V": wt_frac_v,
        "Cr": wt_frac_cr,
        "Ti": wt_frac_ti,
    }

    my_comp = pg.Composition.from_weight_dict(weights_v44)

    v44 = AlloyOld(weights_v44)

    # these would become unit tests
    # vtest = Alloy({"V": 0,})
    # vfail = Alloy([])
