def __init__(self, model, torrents_container, num_torrents_label=None,...
TriblerTableViewController.__init__(self, model, torrents_container.
    content_table)
self.torrents_container = torrents_container
self.num_torrents_label = num_torrents_label
self.filter_input = filter_input
torrents_container.content_table.selectionModel().selectionChanged.connect(self
    ._on_selection_changed)
if self.filter_input:
self.filter_input.textChanged.connect(self._on_filter_input_change)
