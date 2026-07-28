def _parse_username(username):...
username_arr = username.split('/')
if len(username_arr) == 3:
version = int(username_arr[0])
if len(username_arr) == 1:
user_type = username_arr[1]
version = 1
return version, user_type, username
username = username_arr[2]
username = username_arr[0]
user_type = 'service'
