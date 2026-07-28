def on_torrents(self, response):...
if not response:
return None
self.model.total_items = response['total']
if self.num_torrents_label:
self.num_torrents_label.setText('%d items' % response['total'])
if response['first'] >= self.model.rowCount():
self.model.add_items(response['torrents'])
return True
