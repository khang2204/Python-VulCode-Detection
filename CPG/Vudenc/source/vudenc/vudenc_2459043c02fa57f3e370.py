def oauth_logout_handler(sender_app, user=None):...
"""docstring"""
for remote in oauth.remote_apps.values():
token_delete(remote)
