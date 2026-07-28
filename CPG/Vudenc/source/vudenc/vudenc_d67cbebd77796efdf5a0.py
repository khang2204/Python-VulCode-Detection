def on_quit_button_clicked(self, button):...
for db in self.databases_to_save:
db.database_manager.save_database()
self.quit_dialog.destroy()
self.application.quit()
