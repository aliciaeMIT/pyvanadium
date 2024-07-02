from typing import Annotated, Dict, List, Literal, Optional, Tuple

import attrs
import pinttrs

from pyvanadium.src.datastructs.unit_registry import units

pinttrs.set_unit_registry(units)


@attrs.define
class ExperimentData:
    citation: Dict


@attrs.define
class IrradiationParams:
    dose: pinttrs.field(units=units.dpa)


class ExperimentBuilder:
    pass


if __name__ == "__main__":
    print("hello_world")
