from pyzotero import zotero

my_lib = zotero.Zotero(
    library_id=5447847, library_type="group", api_key="liyC89tlLoWt5xQw8VLZL48J"
)

v_data_lib = zotero.Zotero(
    library_id=5576075, library_type="group", api_key="46P2O1SUngk9foXVEkDMQZap"
)


def getId(item):
    return item["key"]


collects = v_data_lib.collections()


for item in collects:
    print(item["data"]["name"])
    if item["data"]["name"] == "tensile":
        tensile_data = item
    elif item["data"]["name"] == "a test for pyzotero":
        test_collection = item
    else:
        continue


tmp = v_data_lib.items(tag="example tag")


# print(v_data_lib.num_collectionitems(collection=test_collection['key']))
print(v_data_lib.num_collectionitems(collection=getId(test_collection)))

# v_data_lib.add_parameters(itemType='-attachment')

its = v_data_lib.collection_items(getId(test_collection))
# v_data_lib.children(tensile_data)


paper = v_data_lib.item("WD2W88YQ")

paper_parent = v_data_lib.item(paper["data"]["parentItem"])


for item in its:
    print(v_data_lib.item_tags(item["key"]))
    print(item["data"]["itemType"])


print(v_data_lib.num_collectionitems(collection=getId(tensile_data)))
print(v_data_lib.key_info())


# items = my_lib.top(limit=5)
# we've retrieved the latest five top-level items in our library
# we can print each item's item type and ID
# for item in items:
#   #print('Item Type: %s | Key: %s' % (item['data']['itemType'],
#   item['data']['key']))
#    print(item['data']['title'])
#   print(item['data']['citekey'])

# print(items[0])
