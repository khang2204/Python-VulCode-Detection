def unlock_database(self):...
self.builder = Gtk.Builder()
self.builder.add_from_resource('/run/terminal/KeepassGtk/unlock_database.ui')
self.set_headerbar()
self.assemble_stack()
self.connect_events()
