def authenticator(key):...
"""docstring"""
request = pyramid.request.Request({'HTTP_COOKIE': '{0}={1}'.format(config.
    registry.settings['session.cookie_name'], key)})
session_data = session_factory(request)
return session_data and session_data.get('admin')
