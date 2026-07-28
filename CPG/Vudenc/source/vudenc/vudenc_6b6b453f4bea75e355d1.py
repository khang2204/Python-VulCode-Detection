def __init__(self, model, table_view, num_channels_label=None, filter_input...
TriblerTableViewController.__init__(self, model, table_view)
self.num_channels_label = num_channels_label
self.filter_input = filter_input
if self.filter_input:
self.filter_input.textChanged.connect(self._on_filter_input_change)
