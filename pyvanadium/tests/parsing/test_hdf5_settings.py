import h5py as h5
import pytest

import pyvanadium.src.parsing.hdf5_settings as hdf5_settings


def test_enable_object_creation_order_tracking():
    hdf5_settings.enable_object_creation_order_tracking()
    assert h5.get_config().track_order
