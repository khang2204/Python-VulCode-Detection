def on_save_check_button_toggled(self, check_button, db):...
if check_button.get_active():
self.databases_to_save.append(db)
self.databases_to_save.remove(db)
