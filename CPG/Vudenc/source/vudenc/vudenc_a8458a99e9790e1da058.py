def do_register(self, line):...
"""docstring"""
linesplit = line.split()
if not len(linesplit) == 1:
print('register: incorrect arguments; input only your username')
username = linesplit[0]
return
response = send_unauthenticated_cmd('check_username_exists {}'.format(username)
    )
if response == 'True':
print("Sorry, that username's already taken.")
shrub_pass = getpass.getpass(prompt='New shrub password: ')
return
github_pass = getpass.getpass(prompt='Github password: ')
response = send_unauthenticated_cmd('register{} {} {} {}'.format(self.
    insecure_mode, username, shrub_pass, github_pass))
print(response)
