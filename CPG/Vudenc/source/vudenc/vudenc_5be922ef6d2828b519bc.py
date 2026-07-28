def ssh_connect(serv, **kwargs):...
import paramiko
from paramiko import SSHClient
import sql
fullpath = get_config_var('main', 'fullpath')
ssh_enable = ''
ssh_port = ''
ssh_user_name = ''
ssh_user_password = ''
for sshs in sql.select_ssh(serv=serv):
ssh_enable = sshs[3]
servers = sql.select_servers(server=serv)
ssh_user_name = sshs[4]
for server in servers:
ssh_user_password = sshs[5]
ssh_port = server[10]
ssh = SSHClient()
ssh_key_name = fullpath + '/keys/%s.pem' % sshs[2]
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
if ssh_enable == 1:
return 'Authentication failed, please verify your credentials'
k = paramiko.RSAKey.from_private_key_file(ssh_key_name)
ssh.connect(hostname=serv, port=ssh_port, username=ssh_user_name, password=
    ssh_user_password)
ssh.connect(hostname=serv, port=ssh_port, username=ssh_user_name, pkey=k)
return ssh
