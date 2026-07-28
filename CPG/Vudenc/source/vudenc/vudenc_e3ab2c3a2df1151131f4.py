def load_torrents(self, start=None, end=None):...
"""docstring"""
if not start and not end:
start, end = self.model.rowCount() + 1, self.model.rowCount(
    ) + self.model.item_load_batch
if self.filter_input and self.filter_input.text().lower():
filter_text = self.filter_input.text().lower()
filter_text = ''
sort_by, sort_asc = self._get_sort_parameters()
self.request_mgr = TriblerRequestManager()
self.request_mgr.perform_request('metadata/channels/%s/torrents' % self.
    model.channel_pk, self.on_torrents, url_params={'first': start, 'last':
    end, 'sort_by': sort_by, 'sort_asc': sort_asc, 'hide_xxx': self.model.
    hide_xxx, 'filter': to_fts_query(filter_text)})
