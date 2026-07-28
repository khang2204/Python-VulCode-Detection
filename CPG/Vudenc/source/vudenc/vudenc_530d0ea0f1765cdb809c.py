def install_haproxy(serv, **kwargs):...
import sql
script = 'install_haproxy.sh'
tmp_config_path = sql.get_setting('tmp_config_path')
haproxy_sock_port = sql.get_setting('haproxy_sock_port')
stats_port = sql.get_setting('stats_port')
server_state_file = sql.get_setting('server_state_file')
stats_user = sql.get_setting('stats_user')
stats_password = sql.get_setting('stats_password')
proxy = sql.get_setting('proxy')
os.system('cp scripts/%s .' % script)
proxy_serv = proxy if proxy is not None else ''
commands = ['sudo chmod +x ' + tmp_config_path + script + ' && ' +
    tmp_config_path + '/' + script + ' PROXY=' + proxy_serv + ' SOCK_PORT=' +
    haproxy_sock_port + ' STAT_PORT=' + stats_port + ' STAT_FILE=' +
    server_state_file + ' STATS_USER=' + stats_user + ' STATS_PASS=' +
    stats_password]
error = str(upload(serv, tmp_config_path, script))
if error:
print('error: ' + error)
os.system('rm -f %s' % script)
ssh_command(serv, commands, print_out='1')
if kwargs.get('syn_flood') == '1':
syn_flood_protect(serv)
