def add_items(self, new_data_items):...
if not new_data_items:
return
old_end = self.rowCount()
new_end = self.rowCount() + len(new_data_items)
self.beginInsertRows(QModelIndex(), old_end, new_end - 1)
self.data_items.extend(new_data_items)
self.endInsertRows()
