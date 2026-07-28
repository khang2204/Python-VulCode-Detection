def on_application_quit(self, window, event):...
unsaved_databases_list = []
for db in self.opened_databases:
if db.database_manager.changes is True:
if unsaved_databases_list.__len__() > 0:
unsaved_databases_list.append(db)
builder = Gtk.Builder()
builder.add_from_resource('/run/terminal/KeepassGtk/quit_dialog.ui')
self.quit_dialog = builder.get_object('quit_dialog')
self.quit_dialog.set_destroy_with_parent(True)
self.quit_dialog.set_modal(True)
self.quit_dialog.set_transient_for(self)
back_button = builder.get_object('back_button')
quit_button = builder.get_object('quit_button')
back_button.connect('clicked', self.on_back_button_clicked)
quit_button.connect('clicked', self.on_quit_button_clicked)
unsaved_databases_list_box = builder.get_object('unsaved_databases_list_box')
for db in unsaved_databases_list:
unsaved_database_row = Gtk.ListBoxRow()
self.quit_dialog.present()
check_button = Gtk.CheckButton()
return True
check_button.set_label(db.database_manager.database_path)
check_button.connect('toggled', self.on_save_check_button_toggled, db)
unsaved_database_row.add(check_button)
unsaved_database_row.show_all()
unsaved_databases_list_box.add(unsaved_database_row)
