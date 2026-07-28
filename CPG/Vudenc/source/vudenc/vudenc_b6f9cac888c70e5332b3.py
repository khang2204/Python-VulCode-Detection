def __init__(self, model, table_view, details_container,...
TriblerTableViewController.__init__(self, model, table_view)
self.num_search_results_label = num_search_results_label
self.details_container = details_container
self.query = None
table_view.selectionModel().selectionChanged.connect(self._on_selection_changed
    )
