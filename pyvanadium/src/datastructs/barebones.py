from typing import Annotated, Dict, List, Literal, Optional, Tuple

import attrs
import pinttr.converters
import pinttrs
import pydantic as pdt
from pint import Quantity

from pyvanadium.src.datastructs import unit_registry
from pyvanadium.src.parsing.zotero import (
    get_vanadium_zotero_database,
    get_zotero_item_from_attachment_key,
)

units = unit_registry.get_unit_registry()

pinttrs.set_unit_registry(units)


@attrs.define
class ExperimentData:
    citation: Dict


@attrs.define
class IrradiationParams:
    dose: pinttrs.field(units=units.dpa)
    material: None


if __name__ == "__main__":
    v_lib = get_vanadium_zotero_database()

    attachment_key = "WD2W88YQ"
    paper = get_zotero_item_from_attachment_key(v_lib, attachment_key)

    my_data = ExperimentData(citation=paper)

    params = IrradiationParams(dose=7.5 * units.dpa)

    print("done")
