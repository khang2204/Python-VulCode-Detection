def assemble_window(self):...
self.set_default_size(800, 500)
self.create_headerbar()
self.first_start_screen()
self.connect('delete-event', self.on_application_quit)
self.custom_css()
