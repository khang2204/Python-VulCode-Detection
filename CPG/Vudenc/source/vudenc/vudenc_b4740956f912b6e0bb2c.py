def reply(self, path, env=None, status=200):...
"""docstring"""
env = (env or {}).copy()
env.setdefault('css_file', None)
env.setdefault('js_file', None)
env.setdefault('navbar_tab_id', None)
env.setdefault('page_title', 'Untitled')
user = self.get_current_user()
common = {'account_picture': user.picture() if user else None,
    'auth_service_config_locked': False, 'is_admin': api.is_admin(),
    'login_url': self.create_login_url(self.request.url), 'logout_url':
    self.create_logout_url('/'), 'using_gae_auth': self.auth_method ==
    handler.gae_cookie_authentication, 'xsrf_token': self.generate_xsrf_token()
    }
if _ui_data_callback:
common.update(_ui_data_callback())
js_module_name = None
if env['js_file']:
assert env['js_file'].endswith('.js')
js_config = {'identity': api.get_current_identity().to_bytes()}
js_module_name = os.path.basename(env['js_file'])[:-3]
js_config.update(common)
full_env = {'app_name': _ui_app_name, 'app_revision_url': utils.
    get_app_revision_url(), 'app_version': utils.get_app_version(),
    'config': json.dumps(js_config), 'csp_nonce': self.csp_nonce,
    'identity': api.get_current_identity(), 'js_module_name':
    js_module_name, 'navbar': [(cls.navbar_tab_id, cls.navbar_tab_title,
    cls.navbar_tab_url) for cls in _ui_navbar_tabs if cls.is_visible()]}
full_env.update(common)
full_env.update(env)
self.response.set_status(status)
self.response.headers['Content-Type'] = 'text/html; charset=utf-8'
self.response.write(template.render(path, full_env))
