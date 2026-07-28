def configure_ui(app_name, ui_tabs=None, ui_data_callback=None):...
"""docstring"""
_ui_app_name = app_name
_ui_data_callback = ui_data_callback
if ui_tabs is not None:
assert all(issubclass(cls, UINavbarTabHandler) for cls in ui_tabs)
template.bootstrap({'auth': TEMPLATES_DIR})
_ui_navbar_tabs = tuple(ui_tabs)
