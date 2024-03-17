import h5py as h5
import hdf5_settings


def extract_group_names(group):
    return list(group.keys())


def print_tree(name, obj):
    full_name = name.split("/")
    # get offset spacing from the full name
    offset = "    "
    depth = len(full_name)

    if isinstance(obj, h5.Dataset):
        # node is a dataset
        print("   " + offset * (depth) + "└──[" + name.split("/")[-1] + "]")
    else:
        print("   " + offset * depth + name.split("/")[-1])


# └──
def print_group_structure(grp):
    print("")
    print("├──" + grp.name.split("/")[-1])
    grp.visititems(print_tree)


def print_structure(grp):
    # base = extract_group_names(grp)

    for key, value in grp.items():
        print("├── " + key)
        value.visititems(print_tree)


if __name__ == "__main__":
    # general comment: we use `with` syntax to open hdf5 files so that we do
    # not need to worry about explicitly closing the file at the end of our
    # usage. So, this note is for anyone new to working with hdf5 files
    # and/or h5py: if you open an h5 file using standard file open syntax,
    # you must explicitly close the file to ensure the hdf5 file does not get
    # corrupted by not being closed.
    with h5.File("../../../database_design/test.h5", "r") as f:
        names = extract_group_names(f)

        # print_structure(f)
        print_structure(f)
        # f.visititems(print_tree)

        if "Vanadium alloys" in f.keys():
            valloys = f["Vanadium alloys"]
            # print_group_structure(valloys)
