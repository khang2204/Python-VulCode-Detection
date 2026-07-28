def __init__(self, *args, **kwargs):...
super().__init__(*args, **kwargs)
keepassgtk.config_manager.configure()
self.assemble_window()
