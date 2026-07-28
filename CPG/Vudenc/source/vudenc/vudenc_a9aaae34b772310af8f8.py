def start_database_opening_routine(self, tab_title, filepath):...
builder = Gtk.Builder()
builder.add_from_resource('/run/terminal/KeepassGtk/create_database.ui')
headerbar = builder.get_object('headerbar')
UnlockDatabase(self, self.create_tab(tab_title, headerbar), filepath)
