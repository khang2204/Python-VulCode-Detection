def start_database_creation_routine(self, tab_title):...
self.database_manager = DatabaseManager(self.filechooser_creation_dialog.
    get_filename(), 'liufhre86ewoiwejmrcu8owe')
builder = Gtk.Builder()
builder.add_from_resource('/run/terminal/KeepassGtk/create_database.ui')
headerbar = builder.get_object('headerbar')
CreateDatabase(self, self.create_tab(tab_title, headerbar), self.
    database_manager)
