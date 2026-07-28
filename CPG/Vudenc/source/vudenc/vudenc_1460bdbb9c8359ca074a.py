def on_tab_close_button_clicked(self, sender, widget):...
page_num = self.container.page_num(widget)
for db in self.opened_databases:
if db.window.container.page_num(db.parent_widget) == page_num:
self.container.remove_page(page_num)
self.opened_databases.remove(db)
self.update_tab_bar_visibility()
