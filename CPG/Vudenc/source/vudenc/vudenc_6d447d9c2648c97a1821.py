def on_password_unlock_button_clicked(self, widget):...
password_unlock_entry = self.builder.get_object('password_unlock_entry')
if password_unlock_entry.get_text() != '':
self.database_manager = DatabaseManager(self.database_filepath,
    password_unlock_entry.get_text())
self.show_unlock_failed_revealer()
self.open_database_page()
password_unlock_entry.grab_focus()
self.logging_manager.log_debug('Opening of database was successfull')
password_unlock_entry.get_style_context().add_class('error')
self.clear_input_fields()
self.logging_manager.log_debug('Could not open database, wrong password')
