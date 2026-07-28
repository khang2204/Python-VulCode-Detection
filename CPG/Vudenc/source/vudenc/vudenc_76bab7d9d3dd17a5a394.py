def check_login(**kwargs):...
import sql
import http.cookies
cookie = http.cookies.SimpleCookie(os.environ.get('HTTP_COOKIE'))
user_uuid = cookie.get('uuid')
ref = os.environ.get('SCRIPT_NAME')
sql.delete_old_uuid()
if user_uuid is not None:
sql.update_last_act_user(user_uuid.value)
print('<meta http-equiv="refresh" content="0; url=login.py?ref=%s">' % ref)
if sql.get_user_name_by_uuid(user_uuid.value) is None:
print('<meta http-equiv="refresh" content="0; url=login.py?ref=%s">' % ref)
