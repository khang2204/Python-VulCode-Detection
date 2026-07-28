def user_is_user_type(user_type):...
if not app.config.get('USE_AUTH'):
return True
if user_type == g.user_type:
return True
return False
