@wraps(f)...
if with_response:
return f(args[0], remote, *args[1:], **kwargs)
return f(remote, *args, **kwargs)
