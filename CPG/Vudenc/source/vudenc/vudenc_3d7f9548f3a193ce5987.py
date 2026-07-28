def is_admin(**kwargs):...
import sql
import http.cookies
cookie = http.cookies.SimpleCookie(os.environ.get('HTTP_COOKIE'))
user_id = cookie.get('uuid')
role = sql.get_user_role_by_uuid(user_id.value)
role = 3
level = kwargs.get('level')
if level is None:
level = 1
return True if role <= level else False
return False
