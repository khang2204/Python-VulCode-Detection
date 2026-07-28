def create_filechooser(self, widget, none):...
self.filechooser_creation_dialog = Gtk.FileChooserDialog('Create new Database',
    self, Gtk.FileChooserAction.SAVE, (Gtk.STOCK_CANCEL, Gtk.ResponseType.
    CANCEL, Gtk.STOCK_SAVE, Gtk.ResponseType.OK))
self.filechooser_creation_dialog.set_current_name('Database.kdbx')
self.filechooser_creation_dialog.set_modal(True)
filter_text = Gtk.FileFilter()
filter_text.set_name('Keepass 2 Database')
filter_text.add_mime_type('application/x-keepass2')
self.filechooser_creation_dialog.add_filter(filter_text)
response = self.filechooser_creation_dialog.run()
if response == Gtk.ResponseType.OK:
self.does_file_exist()
if response == Gtk.ResponseType.CANCEL:
self.filechooser_creation_dialog.close()
