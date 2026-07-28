def on_override_button_clicked(self, widget):...
self.copy_database_file()
tab_title = self.create_tab_title_from_filepath(self.
    filechooser_creation_dialog.get_current_name())
self.start_database_creation_routine(tab_title)
self.override_dialog.destroy()
