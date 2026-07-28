def upload(serv, path, file, **kwargs):...
error = ''
full_path = path + file
if kwargs.get('dir') == 'fullpath':
full_path = path
ssh = ssh_connect(serv)
error = e
sftp = ssh.open_sftp()
error = e
return error
file = sftp.put(file, full_path)
sftp.close()
ssh.close()
