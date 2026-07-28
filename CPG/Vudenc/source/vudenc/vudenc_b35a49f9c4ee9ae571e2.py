def custom_css(self):...
screen = Gdk.Screen.get_default()
css_provider = Gtk.CssProvider()
css_provider_resource = Gio.File.new_for_uri(
    'resource:///run/terminal/KeepassGtk/keepassgtk.css')
css_provider.load_from_file(css_provider_resource)
context = Gtk.StyleContext()
context.add_provider_for_screen(screen, css_provider, Gtk.
    STYLE_PROVIDER_PRIORITY_USER)
