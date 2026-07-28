def check_request(request, user):...
if request.get('token'):
return check_token(request.get('token'))
if user:
return check_email(user.email()) or check_user_id(user.user_id())
