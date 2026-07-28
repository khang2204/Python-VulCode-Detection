def __init__(self, hide_xxx=False):...
RemoteTableModel.__init__(self, parent=None)
self.data_items = []
self.column_position = {name: i for i, name in enumerate(self.columns)}
self.edit_enabled = False
self.hide_xxx = hide_xxx
