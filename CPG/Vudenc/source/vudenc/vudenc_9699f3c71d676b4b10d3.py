def on_GET_request_setup_csrf_cookie(ev):...
"""docstring"""
if ev.request.method == 'GET':
token = ev.request.session.get_csrf_token()
if ev.request.cookies.get('XSRF-TOKEN') != token:
ev.response.set_cookie(COOKIE_NAME, token)
