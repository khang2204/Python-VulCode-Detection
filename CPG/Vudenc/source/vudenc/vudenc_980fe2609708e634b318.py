def auth_add_user(email, password):...
user_id = db.incr('user:ids')
db.hset('user:emails', email, user_id)
db.hmset('user:%s' % user_id, {'user_id': user_id, 'email': email,
    'password_hash': password})
return auth_get_user_by_id(user_id)
