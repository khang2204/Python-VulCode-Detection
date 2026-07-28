def reply(self, path, env=None, status=200):...
"""docstring"""
full_env = {'app_name': _ui_app_name, 'csp_nonce': self.csp_nonce,
    'identity': api.get_current_identity(), 'logout_url': json.dumps(self.
    create_logout_url('/')), 'xsrf_token': self.generate_xsrf_token()}
full_env.update(env or {})
self.response.set_status(status)
self.response.headers['Content-Type'] = 'text/html; charset=utf-8'
self.response.write(template.render(path, full_env))
