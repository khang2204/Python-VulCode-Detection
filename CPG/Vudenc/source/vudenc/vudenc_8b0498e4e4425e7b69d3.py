def check_haproxy_config(serv):...
import sql
commands = ['haproxy  -q -c -f %s' % sql.get_setting('haproxy_config_path')]
ssh = ssh_connect(serv)
for command in commands:
stdin, stdout, stderr = ssh.exec_command(command, get_pty=True)
ssh.close()
if not stderr.read():
return True
return False
