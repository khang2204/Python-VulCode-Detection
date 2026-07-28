@redirect_ui_on_replica...
"""docstring"""
env = {'css_file': self.css_file, 'js_file': self.js_file_url,
    'navbar_tab_id': self.navbar_tab_id, 'page_title': self.navbar_tab_title}
self.reply(self.template_file, env)
