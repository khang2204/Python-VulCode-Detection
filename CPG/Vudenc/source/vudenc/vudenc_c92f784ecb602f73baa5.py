def redirect_to_logout_if_no_auth(f):...
"""docstring"""
@wraps(f)...
if user_mod.is_expired():
return user_mod.redirect_to_goodbye()
if user_mod.is_authenticated():
return f(*args, **kwargs)
return user_mod.redirect_to_goodbye()
