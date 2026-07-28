def open_database_page(self):...
self.clear_input_fields()
keepassgtk.config_manager.create_config_entry_string('history',
    'last-opened-db', str(self.database_filepath))
keepassgtk.config_manager.save_config()
self.unlock_database_stack_box.destroy()
UnlockedDatabase(self.window, self.parent_widget, self.database_manager)
