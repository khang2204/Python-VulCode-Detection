def open_filechooser(self, widget, none):...
filechooser_opening_dialog = Gtk.FileChooserDialog('Choose Keepass Database',
    self, Gtk.FileChooserAction.OPEN, (Gtk.STOCK_CANCEL, Gtk.ResponseType.
    CANCEL, Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
filter_text = Gtk.FileFilter()
filter_text.set_name('Keepass 2 Database')
filter_text.add_mime_type('application/x-keepass2')
filechooser_opening_dialog.add_filter(filter_text)
response = filechooser_opening_dialog.run()
if response == Gtk.ResponseType.OK:
self.logging_manager.log_debug('File selected: ' +
    filechooser_opening_dialog.get_filename())
if response == Gtk.ResponseType.CANCEL:
filechooser_opening_dialog.close()
self.logging_manager.log_debug('File selection canceled')
tab_title = self.create_tab_title_from_filepath(filechooser_opening_dialog.
    get_filename())
filechooser_opening_dialog.close()
self.start_database_opening_routine(tab_title, filechooser_opening_dialog.
    get_filename())
