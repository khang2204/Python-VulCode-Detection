def __init__(self):...
self.authomatic_config = {'google': {'class_': oauth2.Google,
    'consumer_key': app.config['GOOGLE_OAUTH_CLIENT_ID'], 'consumer_secret':
    app.config['GOOGLE_OAUTH_CONSUMER_SECRET'], 'scope': ['profile', 'email']}}
self.authomatic = Authomatic(self.authomatic_config, app.config[
    'AUTHOMATIC_SALT'])
