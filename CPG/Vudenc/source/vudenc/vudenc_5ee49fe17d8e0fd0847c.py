def check_and_log(request, user):...
auth = check_request(request, user)
logging.info('access.py: ' + (auth and 'authorized %s' % auth.description or
    'not authorized') + ' (token=%r, user=%r)' % (request.get('token'), 
    user and user.email()))
if not auth and user:
auth = Authorization(description=user.nickname(), email=user.email())
return auth
