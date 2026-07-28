def _check_flags(self):...
"""docstring"""
required_flags = ['hp3par_api_url', 'hp3par_username', 'hp3par_password',
    'san_ip', 'san_login', 'san_password']
self.common.check_flags(self.configuration, required_flags)
