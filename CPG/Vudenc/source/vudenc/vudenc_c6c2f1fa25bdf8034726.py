def _on_selection_changed(self, _):...
selected_indices = self.table_view.selectedIndexes()
if not selected_indices:
return
self.torrents_container.details_container.show()
torrent_info = selected_indices[0].model().data_items[selected_indices[0].row()
    ]
self.torrents_container.details_tab_widget.update_with_torrent(selected_indices
    [0], torrent_info)
