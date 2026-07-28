def data(self, index, role):...
if role == Qt.DisplayRole:
column = self.columns[index.column()]
data = self.data_items[index.row()][column] if column in self.data_items[
    index.row()] else u'UNDEFINED'
return self.column_display_filters.get(column, str(data))(data
    ) if column in self.column_display_filters else data
