def on_keyfile_unlock_button_clicked(self, widget):...
keyfile_unlock_select_button = self.builder.get_object(
    'keyfile_unlock_select_button')
keyfile_path = keyfile_unlock_select_button.get_label()
self.database_manager = DatabaseManager(self.database_filepath, password=
    None, keyfile=keyfile_path)
self.show_unlock_failed_revealer()
self.open_database_page()
keyfile_unlock_select_button.get_style_context().add_class(Gtk.
    STYLE_CLASS_DESTRUCTIVE_ACTION)
self.logging_manager.log_debug('Database successfully opened with keyfile')
keyfile_unlock_select_button.set_label('Try again')
self.logging_manager.log_debug('Invalid keyfile chosen')
self.logging_manager.log_debug('Keyfile path: ' + keyfile_path)
