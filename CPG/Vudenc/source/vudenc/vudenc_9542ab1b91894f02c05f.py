def connect_events(self):...
password_unlock_button = self.builder.get_object('password_unlock_button')
password_unlock_button.connect('clicked', self.
    on_password_unlock_button_clicked)
keyfile_unlock_button = self.builder.get_object('keyfile_unlock_button')
keyfile_unlock_button.connect('clicked', self.on_keyfile_unlock_button_clicked)
composite_unlock_button = self.builder.get_object('composite_unlock_button')
composite_unlock_button.connect('clicked', self.
    on_composite_unlock_button_clicked)
keyfile_unlock_select_button = self.builder.get_object(
    'keyfile_unlock_select_button')
keyfile_unlock_select_button.connect('clicked', self.
    on_keyfile_unlock_select_button_clicked)
composite_unlock_select_button = self.builder.get_object(
    'composite_unlock_select_button')
composite_unlock_select_button.connect('clicked', self.
    on_composite_unlock_select_button_clicked)
password_unlock_entry = self.builder.get_object('password_unlock_entry')
password_unlock_entry.connect('activate', self.
    on_password_unlock_button_clicked)
password_unlock_entry.connect('icon-press', self.
    on_password_unlock_entry_secondary_clicked)
