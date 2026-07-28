def create_tab(self, title, headerbar):...
if self.container == NotImplemented:
self.create_container()
page_instance = ContainerPage(headerbar)
tab_hbox = Gtk.HBox(False, 0)
tab_label = Gtk.Label(title)
tab_hbox.pack_start(tab_label, False, False, False)
icon = Gio.ThemedIcon(name='window-close-symbolic')
close_image = Gtk.Image.new_from_gicon(icon, Gtk.IconSize.BUTTON)
close_button = Gtk.Button()
close_button.set_relief(Gtk.ReliefStyle.NONE)
close_button.set_focus_on_click(False)
close_button.connect('clicked', self.on_tab_close_button_clicked, page_instance
    )
close_button.add(close_image)
tab_hbox.pack_start(close_button, False, False, False)
tab_hbox.show_all()
self.container.append_page(page_instance, tab_hbox)
self.container.set_current_page(self.container.page_num(page_instance))
self.update_tab_bar_visibility()
return page_instance
