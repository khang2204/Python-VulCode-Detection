def authentication_error(self, error):...
"""docstring"""
env = {'page_title': 'Access Denied', 'error': error}
self.reply('auth/admin/access_denied.html', env=env, status=401)
