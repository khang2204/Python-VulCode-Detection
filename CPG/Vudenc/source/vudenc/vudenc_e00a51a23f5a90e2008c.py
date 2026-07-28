def _on_selection_changed(self, _):...
selected_indices = self.table_view.selectedIndexes()
if not selected_indices:
return
torrent_info = selected_indices[0].model().data_items[selected_indices[0].row()
    ]
if torrent_info['type'] == 'channel':
self.details_container.hide()
self.details_container.show()
self.table_view.clearSelection()
self.details_container.details_tab_widget.update_with_torrent(selected_indices
    [0], torrent_info)
return
