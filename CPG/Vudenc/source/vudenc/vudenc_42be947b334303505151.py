def do_edit_issue(self, line):...
if not self.logged_in():
print('shrub: unauthenticated; use "login [username] to log in first')
response = self.send_cmd('edit_issue{} {}'.format(self.insecure_mode, line))
return
print(response)
