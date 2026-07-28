def auth_get_user_by_email(email):...
user_id = db.hget('user:emails', email)
if not user_id:
return None
return auth_get_user_by_id(user_id)
