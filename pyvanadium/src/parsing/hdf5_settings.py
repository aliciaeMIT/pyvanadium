import h5py as h5


def enable_object_creation_order_tracking():
    """
    Turn on creation order tracking, so that the resulting HDF file does not
    get sorted alphanumerically. For end-user convenience, we want to have a
    consistent organization of the first level groups that makes sense for easy
    navigation.
    """
    h5.get_config().track_order = True

    return h5.get_config().track_order


# By default, we want this to be enabled, so this should run when the file is
# imported.
enable_object_creation_order_tracking()
