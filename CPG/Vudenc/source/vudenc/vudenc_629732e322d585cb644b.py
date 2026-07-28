def user_is_service(service):...
if not app.config.get('USE_AUTH'):
return True
if g.username == service:
return True
return False
