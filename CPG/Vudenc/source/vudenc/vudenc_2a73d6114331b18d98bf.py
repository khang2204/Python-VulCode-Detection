def do_login(self, line):...
"""docstring"""
if self.logged_in():
print(
    'shrub: login: already logged in; restart shrub to login as a different user'
    )
linesplit = line.split()
return
if not len(linesplit) == 1:
print('login: incorrect arguments; input only your username')
username = linesplit[0]
return
password = getpass.getpass()
response = send_unauthenticated_cmd('check_login {} {}'.format(username,
    password))
if response == 'True':
print('Success: now logged in as {}.'.format(username))
print('shrub: login: authentication failure')
self.user_creds = [username, password]
