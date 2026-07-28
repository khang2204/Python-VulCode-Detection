def send_cmd(self, command_string):...
if not self.logged_in():
exit('send_cmd called before login')
client = open_ssh_client()
stdin, stdout, stderr = client.exec_command('shrubbery {} {} '.format(self.
    user_creds[0], self.user_creds[1]) + command_string)
print('***stdout: ' + stdout.read().decode('utf-8'))
print('***stderr: ' + stderr.read().decode('utf-8'))
return stdout.read().decode('utf-8')
