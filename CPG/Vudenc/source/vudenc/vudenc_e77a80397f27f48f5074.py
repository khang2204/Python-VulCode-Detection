def on_keyfile_unlock_select_button_clicked(self, widget):...
keyfile_chooser_dialog = Gtk.FileChooserDialog('Choose a keyfile', self.
    window, Gtk.FileChooserAction.OPEN, (Gtk.STOCK_CANCEL, Gtk.ResponseType
    .CANCEL, Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
filter_text = Gtk.FileFilter()
filter_text.set_name('Keyfile')
filter_text.add_mime_type('application/octet-stream')
filter_text.add_mime_type('application/x-keepass2')
filter_text.add_mime_type('text/plain')
filter_text.add_mime_type('application/x-iwork-keynote-sffkey')
keyfile_chooser_dialog.add_filter(filter_text)
response = keyfile_chooser_dialog.run()
if response == Gtk.ResponseType.OK:
self.logging_manager.log_debug('File selected: ' + keyfile_chooser_dialog.
    get_filename())
if response == Gtk.ResponseType.CANCEL:
keyfile_chooser_dialog.close()
self.logging_manager.log_debug('File selection canceled')
keyfile_unlock_select_button = self.builder.get_object(
    'keyfile_unlock_select_button')
keyfile_chooser_dialog.close()
keyfile_unlock_select_button.get_style_context().remove_class(Gtk.
    STYLE_CLASS_DESTRUCTIVE_ACTION)
keyfile_unlock_select_button.get_style_context().add_class(Gtk.
    STYLE_CLASS_SUGGESTED_ACTION)
keyfile_unlock_select_button.set_label(ntpath.basename(
    keyfile_chooser_dialog.get_filename()))
