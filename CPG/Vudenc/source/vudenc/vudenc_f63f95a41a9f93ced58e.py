def add_items(self, new_data_items):...
super(TriblerContentModel, self).add_items(new_data_items)
items_len = len(self.data_items)
new_items_len = len(new_data_items)
for i, item in enumerate(new_data_items):
if 'infohash' in item:
self.infohashes[item['infohash']] = items_len - new_items_len + i
