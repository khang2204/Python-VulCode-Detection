def on_channels(self, response):...
if not response:
return
self.model.total_items = response['total']
if self.num_channels_label:
self.num_channels_label.setText('%d items' % response['total'])
if response['first'] >= self.model.rowCount():
self.model.add_items(response['channels'])
