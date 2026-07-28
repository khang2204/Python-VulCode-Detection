def auth_get_user_by_id(user_id):...
key = 'user:%s' % user_id
if db.hlen(key) == 0:
return None
user_data = db.hgetall(key)
user = User()
user.user_id = user_data['user_id']
user.email = user_data['email']
user.password_hash = generate_password_hash(user_data['password_hash'])
return user
