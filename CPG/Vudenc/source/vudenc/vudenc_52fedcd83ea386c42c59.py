def copy_database_file(self):...
stock_database = Gio.File.new_for_uri(
    'resource:///run/terminal/KeepassGtk/database.kdbx')
new_database = Gio.File.new_for_path(self.filechooser_creation_dialog.
    get_filename())
stock_database.copy(new_database, Gio.FileCopyFlags.OVERWRITE)
self.filechooser_creation_dialog.close()
