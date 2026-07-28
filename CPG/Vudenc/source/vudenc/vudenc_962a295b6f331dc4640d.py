def add_user(**kwargs):...
r = admin_req('users/add', args=kwargs)
g = re.search('/user/([0-9]+)$', r.url)
if g:
user_id = int(g.group(1))
kwargs['user_id'] = user_id
created_users[user_id] = kwargs
r = admin_req('contest/' + kwargs['contest_id'] + '/users/add', args=kwargs)
g = re.search('<input type="radio" name="user_id" value="' + str(user_id) +
    '"/>', r.text)
if g:
return user_id
