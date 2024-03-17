import h5py as h5
import hdf5_settings

# Turn on object creation order tracking
print(hdf5_settings.enable_object_creation_order_tracking())
print(h5.get_config().track_order)


with h5.File("../../../database_design/test.h5", "r") as f:
    print(f.keys())

    if "Raw data" in f.keys():
        rd = f["Raw data"]
        print(rd.keys())

    f.close()
