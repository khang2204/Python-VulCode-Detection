def del_account(self, username):...
"""docstring"""
shellutil.run('> /var/run/utmp')
shellutil.run('/usr/bin/tmsh delete auth user ' + username)
