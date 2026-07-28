def set_headerbar(self):...
headerbar = self.builder.get_object('headerbar')
headerbar.set_subtitle(self.database_filepath)
self.window.set_titlebar(headerbar)
self.parent_widget.set_headerbar(headerbar)
back_button = self.builder.get_object('back_button')
back_button.connect('clicked', self.on_headerbar_back_button_clicked)
