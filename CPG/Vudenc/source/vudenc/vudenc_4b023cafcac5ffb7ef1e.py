def get_logged_in_user():...
"""docstring"""
if hasattr(g, 'username'):
return g.username
if user_mod.is_authenticated():
return user_mod.current_email()
