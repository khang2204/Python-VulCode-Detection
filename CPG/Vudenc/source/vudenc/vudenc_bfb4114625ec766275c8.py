def set_hostname(self, hostname):...
rc_file_path = '/etc/rc.conf'
conf_file = fileutil.read_file(rc_file_path).split('\n')
textutil.set_ini_config(conf_file, 'hostname', hostname)
fileutil.write_file(rc_file_path, '\n'.join(conf_file))
shellutil.run('hostname {0}'.format(hostname), chk_err=False)
