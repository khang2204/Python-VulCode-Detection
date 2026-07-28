def does_file_exist(self):...
if os.path.exists(self.filechooser_creation_dialog.get_filename()):
builder = Gtk.Builder()
self.copy_database_file()
builder.add_from_resource('/run/terminal/KeepassGtk/override_dialog.ui')
tab_title = self.create_tab_title_from_filepath(self.
    filechooser_creation_dialog.get_current_name())
self.override_dialog = builder.get_object('override_dialog')
self.start_database_creation_routine(tab_title)
self.override_dialog.set_destroy_with_parent(True)
self.override_dialog.set_modal(True)
self.override_dialog.set_transient_for(self.filechooser_creation_dialog)
cancel_button = builder.get_object('cancel_button')
override_button = builder.get_object('override_button')
cancel_button.connect('clicked', self.on_cancel_button_clicked)
override_button.connect('clicked', self.on_override_button_clicked)
self.override_dialog.present()
