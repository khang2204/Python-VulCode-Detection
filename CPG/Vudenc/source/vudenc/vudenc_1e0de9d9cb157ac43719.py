def update_torrent_info(self, update_dict):...
row = self.infohashes.get(update_dict['infohash'])
if row:
self.data_items[row].update(**update_dict)
self.dataChanged.emit(self.index(row, 0), self.index(row, len(self.columns)
    ), [])
