def on_torrents(self, response):...
if super(MyTorrentsTableViewController, self).on_torrents(response):
self.table_view.window().edit_channel_page.channel_dirty = response['dirty']
self.table_view.window().edit_channel_page.update_channel_commit_views()
