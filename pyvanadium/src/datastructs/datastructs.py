import numpy as np
from pyzotero import zotero


class ExperimentData:
    def __init__(self, citekey, zotero_item):
        self.citekey = citekey
        self.zotero_item = zotero_item


class IrradiationData:

    def __init__(self):
        self.temperature = None

    def add_dpa(self, dpa):
        self.dpa = dpa

    def add_temperature(self, T):
        if self.T:
            np.append(self.T, T)


class NeutronIrradiationParams:
    pass


class MechanicalProperties:
    pass


class MechanicalProperty:
    pass


zot = zotero.Zotero(
    library_id=5447847, library_type="group", api_key="liyC89tlLoWt5xQw8VLZL48J"
)


my_experiment = ExperimentData(
    citekey="fukumotoVaryingTemperatureEffects2004", zotero_item="LCVRUL7L"
)
