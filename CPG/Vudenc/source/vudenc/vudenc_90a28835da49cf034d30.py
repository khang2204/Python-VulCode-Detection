def username_to_id(username, query):...
user = query.find_customer(username)
if user is not None:
print('Welcome Back', user[1], user[2])
return create_new_user(username, query)
return user[7]
