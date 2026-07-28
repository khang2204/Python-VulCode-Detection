def on_composite_unlock_button_clicked(self, widget):...
composite_unlock_entry = self.builder.get_object('composite_unlock_entry')
composite_unlock_select_button = self.builder.get_object(
    'composite_unlock_select_button')
if composite_unlock_entry.get_text() is not '':
composite_unlock_entry.get_style_context().add_class('error')
self.database_manager = DatabaseManager(self.database_filepath,
    composite_unlock_entry.get_text(), self.composite_keyfile_path)
self.show_unlock_failed_revealer()
self.open_database_page()
composite_unlock_entry.grab_focus()
self.logging_manager.log_debug('Opening of database was successfull')
composite_unlock_entry.get_style_context().add_class('error')
composite_unlock_select_button.get_style_context().remove_class(
    'suggested-action')
composite_unlock_select_button.get_style_context().add_class(
    'destructive-action')
self.clear_input_fields()
self.logging_manager.log_debug('Could not open database, wrong password')
