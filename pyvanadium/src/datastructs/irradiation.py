# from typing import List, Optional

import pydantic as pdt
import pymatgen.core as pg

from .alloy import Alloy


class IrradiatingParticleBase(pdt.BaseModel):
    energy: float


class Ion(IrradiatingParticleBase):
    """
    todo: update to actual ion with charge state... Specie?
    """

    ion: pg.Element


class Neutron(IrradiatingParticleBase):
    source: str


class Irradiation(pdt.BaseModel):
    particle: IrradiatingParticleBase
    sample: Alloy


class IonBuilder:
    pass


class NeutronBuilder:
    pass


class IrradiationBuilder:
    pass
