def get_config(serv, cfg, **kwargs):...
import sql
config_path = '/etc/keepalived/keepalived.conf' if kwargs.get('keepalived'
    ) else sql.get_setting('haproxy_config_path')
ssh = ssh_connect(serv)
sftp = ssh.open_sftp()
ssh = str(e)
sftp.get(config_path, cfg)
return ssh
sftp.close()
ssh.close()
