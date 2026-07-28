def require_csrf_token(f):...
@wraps(f)...
if not app.config.get('USE_AUTH'):
return f(*args, **kwargs)
if g.auth_type == 'kms':
return f(*args, **kwargs)
if user_mod.check_csrf_token():
return f(*args, **kwargs)
return abort(401)
