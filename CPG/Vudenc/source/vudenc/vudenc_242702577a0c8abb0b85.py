def require_logout_for_goodbye(f):...
@wraps(f)...
if not app.config.get('USE_AUTH'):
return f(*args, **kwargs)
get_logged_in_user()
return f(*args, **kwargs)
logging.warning('require_logout(): calling log_out()')
resp = user_mod.log_out()
if resp.headers.get('Location') == url_for('goodbye'):
return f(*args, **kwargs)
return resp
