def do_delete_comment(self, line):...
if not self.logged_in():
print('shrub: unauthenticated; use "login [username] to log in first')
response = self.send_cmd('delete_comment{} {}'.format(self.insecure_mode, line)
    )
return
print(response)
