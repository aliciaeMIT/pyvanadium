from pyzotero import zotero

# my_lib = zotero.Zotero(library_id=5447847,library_type='group',
#                       api_key='liyC89tlLoWt5xQw8VLZL48J')

# v_data_lib = zotero.Zotero(library_id=5576075, library_type='group',
# api_key='46P2O1SUngk9foXVEkDMQZap')


def get_zotero_id(item):
    return item["key"]


def get_vanadium_zotero_database():
    return zotero.Zotero(
        library_id=5576075, library_type="group", api_key="46P2O1SUngk9foXVEkDMQZap"
    )


def get_zotero_item_from_attachment_key(zotero_lib_instance, key):
    child_item = zotero_lib_instance.item(key)
    parent = zotero_lib_instance.item(child_item["data"]["parentItem"])
    return parent


def get_zotero_lib():
    return zotero.Zotero(
        library_id=11392871, library_type="user", api_key="YeKOvk4toHE7Dog3gAG3ImZt"
    )
