import h5py as h5
import hdf5_settings

# Turn on creation order tracking, so that the resulting HDF file does not
# get sorted alphanumerically. For end-user convenience, we want to have a
# consistent organization of the first level groups that makes sense for easy
# navigation.
h5.get_config().track_order = True
