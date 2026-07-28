def check_csrf_token(self):...
token = request.headers.get('X-XSRF-TOKEN', '')
if not token:
return False
return safe_str_cmp(token, session.get('XSRF-TOKEN', ''))
