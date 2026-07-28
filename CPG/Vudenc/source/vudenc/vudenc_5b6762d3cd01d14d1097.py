def on_composite_unlock_select_button_clicked(self, widget):...
filechooser_opening_dialog = Gtk.FileChooserDialog('Choose Keyfile', self.
    window, Gtk.FileChooserAction.OPEN, (Gtk.STOCK_CANCEL, Gtk.ResponseType
    .CANCEL, Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
composite_unlock_select_button = self.builder.get_object(
    'composite_unlock_select_button')
filter_text = Gtk.FileFilter()
filter_text.set_name('Keyfile')
filter_text.add_mime_type('application/octet-stream')
filter_text.add_mime_type('application/x-keepass2')
filter_text.add_mime_type('text/plain')
filter_text.add_mime_type('application/x-iwork-keynote-sffkey')
filechooser_opening_dialog.add_filter(filter_text)
response = filechooser_opening_dialog.run()
if response == Gtk.ResponseType.OK:
self.logging_manager.log_debug('File selected: ' +
    filechooser_opening_dialog.get_filename())
if response == Gtk.ResponseType.CANCEL:
filechooser_opening_dialog.close()
self.logging_manager.log_debug('File selection cancelled')
file_path = filechooser_opening_dialog.get_filename()
filechooser_opening_dialog.close()
composite_unlock_select_button.set_label(ntpath.basename(file_path))
self.composite_keyfile_path = file_path
