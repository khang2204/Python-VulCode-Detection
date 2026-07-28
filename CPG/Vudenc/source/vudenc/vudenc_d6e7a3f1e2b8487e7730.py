def load_search_results(self, query, start=None, end=None):...
"""docstring"""
self.query = query
if not start or not end:
start, end = self.model.rowCount() + 1, self.model.rowCount(
    ) + self.model.item_load_batch
sort_by, sort_asc = self._get_sort_parameters()
url_params = {'filter': to_fts_query(query), 'first': start if start else
    '', 'last': end if end else '', 'sort_by': sort_by if sort_by else '',
    'sort_asc': sort_asc, 'hide_xxx': self.model.hide_xxx, 'metadata_type':
    self.model.type_filter if self.model.type_filter else ''}
self.request_mgr = TriblerRequestManager()
self.request_mgr.perform_request('search', self.on_search_results,
    url_params=url_params)
