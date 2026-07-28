@property...
"""docstring"""
if not hasattr(self, '_email_whitelist'):
self._email_whitelist = None
return self._email_whitelist
if app.config['USERS_FILE']:
self._email_whitelist = yaml.safe_load(f.read())
