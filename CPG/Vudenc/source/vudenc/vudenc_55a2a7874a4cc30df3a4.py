def __init__(self, parent=None):...
super(RemoteTableModel, self).__init__(parent)
self.data_items = []
self.item_load_batch = 50
self.total_items = 0
self.infohashes = {}
