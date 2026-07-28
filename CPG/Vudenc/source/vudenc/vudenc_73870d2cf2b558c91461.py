def on_password_unlock_entry_secondary_clicked(self, widget, position,...
if widget.get_visibility():
widget.set_invisible_char('●')
widget.set_visibility(True)
widget.set_visibility(False)
