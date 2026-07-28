def send_unauthenticated_cmd(command_string):...
"""docstring"""
client = open_ssh_client()
stdin, stdout, stderr = client.exec_command('shrubbery ' + command_string)
print('***stdout: ' + stdout.read().decode('utf-8'))
print('***stderr: ' + stderr.read().decode('utf-8'))
return stdout.read().decode('utf-8')
