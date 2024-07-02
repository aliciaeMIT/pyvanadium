import h5py as h5
import hdf5_settings
import hdf5_writing

with h5.File("../../../database_design/test.h5", "r") as f:
    print(f.keys())

    if "Raw data" in f.keys():
        rd = f["Raw data"]
        print(rd.keys())

    f.close()
