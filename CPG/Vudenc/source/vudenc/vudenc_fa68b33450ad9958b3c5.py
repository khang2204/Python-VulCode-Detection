def create_headerbar(self):...
builder = Gtk.Builder()
builder.add_from_resource('/run/terminal/KeepassGtk/main_window.ui')
self.headerbar = builder.get_object('headerbar')
file_open_button = builder.get_object('open_button')
file_open_button.connect('clicked', self.open_filechooser, None)
file_new_button = builder.get_object('new_button')
file_new_button.connect('clicked', self.create_filechooser, None)
self.set_titlebar(self.headerbar)
