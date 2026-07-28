def require_login(func):...
async def ret(*args, **kwargs):...
session = await get_session(args[0])
if 'uname' not in session:
session['return_after_login'] = args[0].path_qs
out = await func(*args, **kwargs)
return 'You must be <a href="/login">logged in</a> to access this page.'
return out
