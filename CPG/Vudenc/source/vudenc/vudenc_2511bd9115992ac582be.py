def ssh_command(serv, commands, **kwargs):...
ssh = ssh_connect(serv)
for command in commands:
stdin, stdout, stderr = ssh.exec_command(command, get_pty=True)
if kwargs.get('ip') == '1':
ssh.close()
print("<div class='alert alert-danger' style='margin: 0;'>" + str(ssh) +
    "<a title='Close' id='errorMess'><b>X</b></a></div>")
show_ip(stdout)
if kwargs.get('show_log') == '1':
for line in stderr.read().decode(encoding='UTF-8'):
show_log(stdout)
if kwargs.get('server_status') == '1':
if line:
server_status(stdout)
if kwargs.get('print_out'):
print("<div class='alert alert-warning'>" + line + '</div>')
print(stdout.read().decode(encoding='UTF-8'))
if kwargs.get('retunr_err') == 1:
return stdout.read().decode(encoding='UTF-8')
return stderr.read().decode(encoding='UTF-8')
return stdout.read().decode(encoding='UTF-8')
