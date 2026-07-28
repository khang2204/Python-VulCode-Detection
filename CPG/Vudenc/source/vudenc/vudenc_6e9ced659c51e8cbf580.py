def on_search_results(self, response):...
if not response:
return
self.model.total_items = response['total']
if self.num_search_results_label:
self.num_search_results_label.setText('%d results' % response['total'])
if response['first'] >= self.model.rowCount():
self.model.add_items(response['results'])
