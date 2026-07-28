def make_handler(f, remote, with_response=True):...
"""docstring"""
if isinstance(f, six.text_type):
f = import_string(f)
@wraps(f)...
if with_response:
return f(args[0], remote, *args[1:], **kwargs)
return f(remote, *args, **kwargs)
