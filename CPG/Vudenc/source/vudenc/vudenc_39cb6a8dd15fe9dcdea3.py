def oauth_error_handler(f):...
"""docstring"""
@wraps(f)...
return f(*args, **kwargs)
current_app.logger.warning(e.message, exc_info=True)
return inner
return oauth2_handle_error(e.remote, e.response, e.code, e.uri, e.description)
