def first_start_screen(self):...
if keepassgtk.config_manager.has_group('history'
self.logging_manager.log_debug('Found last opened database entry (' +
    keepassgtk.config_manager.get_string('history', 'last-opened-db') + ')')
self.logging_manager.log_debug(
    'No / Not valid last opened database entry found.')
tab_title = ntpath.basename(keepassgtk.config_manager.get_string('history',
    'last-opened-db'))
builder = Gtk.Builder()
self.start_database_opening_routine(tab_title, keepassgtk.config_manager.
    get_string('history', 'last-opened-db'))
builder.add_from_resource('/run/terminal/KeepassGtk/main_window.ui')
self.first_start_grid = builder.get_object('first_start_grid')
self.add(self.first_start_grid)
