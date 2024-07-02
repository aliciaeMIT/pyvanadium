from typing import Annotated, Dict, List, Literal, Optional, Tuple

import attrs
import pinttrs

from pyvanadium.src.datastructs.composition import Composition
from pyvanadium.src.datastructs.experiment import ExperimentData, IrradiationParams
from pyvanadium.src.datastructs.unit_registry import units
from pyvanadium.src.parsing.zotero import (
    get_vanadium_zotero_database,
    get_zotero_id,
    get_zotero_item_from_attachment_key,
    get_zotero_lib,
)

pinttrs.set_unit_registry(units)


@attrs.define
class Heat:
    id: str
    composition: Composition
    citation: Dict
    citekey: str


@attrs.define
class Sample:
    composition: Composition
    heat: Optional[Heat] = None
    citations: Optional[List] = None


if __name__ == "__main__":
    v_lib = get_vanadium_zotero_database()
    my_lib = get_zotero_lib()
    paper = get_zotero_item_from_attachment_key(v_lib, "WD2W88YQ")

    my_data = ExperimentData(citation=paper)
    params = IrradiationParams(dose=7.5 * units.dpa)

    my_var = 461.0 * units.wppm
    converted = my_var.to(units.wt_pct)

    alloy_comp = {
        "Cr": 3.8 * units.wt_percent,
        "Ti": 3.9 * units.wt_percent,
        "O": 310 * units.wppm,
        "N": 85 * units.wppm,
        "C": 80 * units.wppm,
        "Si": 783 * units.wppm,
    }

    alloying_elems = ["V", "Cr", "Ti"]
    impure = ["O", "N", "C", "Si"]

    my_comp = Composition(
        composition=alloy_comp, alloying_elements=alloying_elems, impurities=impure
    )

    # comp_832665 = Composition()
    paper_832665 = get_zotero_item_from_attachment_key(my_lib, "TZR45X27")
    citekey_832665 = get_zotero_id(paper_832665)

    # doe_heat = Heat(id='832665', composition=None)

    print("done")
