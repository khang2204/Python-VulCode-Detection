def __init__(self, model, table_view):...
self.model = model
self.model.on_sort.connect(self._on_view_sort)
self.table_view = table_view
self.table_view.setModel(self.model)
self.table_view.verticalScrollBar().valueChanged.connect(self._on_list_scroll)
self.request_mgr = None
