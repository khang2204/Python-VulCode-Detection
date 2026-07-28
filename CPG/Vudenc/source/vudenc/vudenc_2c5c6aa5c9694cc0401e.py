@wraps(f)...
if not request.is_xhr:
return abort(401)
return f(*args, **kwargs)
