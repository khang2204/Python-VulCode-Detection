@handler.unsupported_on_local_server...
"""docstring"""
self.render('login.html', {'apiKey': local_config.ProjectConfig().get(
    'firebase.api_key'), 'authDomain': auth.auth_domain(), 'dest': self.
    request.get('dest')})
