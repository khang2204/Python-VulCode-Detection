@wraps(fn)...
token = request.headers.get(HEADER_NAME)
session_token = request.session.get_csrf_token()
if token == session_token:
return fn(context, request)
