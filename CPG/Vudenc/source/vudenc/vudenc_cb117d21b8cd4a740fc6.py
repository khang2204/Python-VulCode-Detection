def create_container(self):...
if self.first_start_grid != NotImplemented:
self.first_start_grid.destroy()
self.container = Gtk.Notebook()
self.container.set_border_width(0)
self.container.set_scrollable(True)
self.container.set_show_border(False)
self.container.connect('switch-page', self.on_tab_switch)
self.add(self.container)
self.show_all()
