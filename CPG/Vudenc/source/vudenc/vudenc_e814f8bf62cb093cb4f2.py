def do_list_repo_issues(self, line):...
if not self.logged_in():
print('shrub: unauthenticated; use "login [username] to log in first')
response = self.send_cmd('list_repo_issues{} {}'.format(self.insecure_mode,
    line))
return
print(response)
