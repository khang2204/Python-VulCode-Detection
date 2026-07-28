def upload_and_restart(serv, cfg, **kwargs):...
import sql
tmp_file = sql.get_setting('tmp_config_path') + '/' + get_data('config'
    ) + '.cfg'
error = ''
os.system('dos2unix ' + cfg)
return 'Please install dos2unix'
if kwargs.get('keepalived') == 1:
if kwargs.get('just_save') == 'save':
if kwargs.get('just_save') == 'test':
commands = ['sudo mv -f ' + tmp_file + ' /etc/keepalived/keepalived.conf']
commands = ['sudo mv -f ' + tmp_file +
    ' /etc/keepalived/keepalived.conf && sudo systemctl restart keepalived']
commands = ['sudo haproxy  -q -c -f ' + tmp_file + '&& sudo rm -f ' + tmp_file]
if kwargs.get('just_save') == 'save':
error += str(upload(serv, tmp_file, cfg, dir='fullpath'))
if sql.get_setting('firewall_enable') == '1':
commands = ['sudo haproxy  -q -c -f ' + tmp_file + '&& sudo mv -f ' +
    tmp_file + ' ' + sql.get_setting('haproxy_config_path')]
commands = ['sudo haproxy  -q -c -f ' + tmp_file + '&& sudo mv -f ' +
    tmp_file + ' ' + sql.get_setting('haproxy_config_path') + ' && sudo ' +
    sql.get_setting('restart_command')]
error += ssh_command(serv, commands)
error += e
if error:
commands.extend(open_port_firewalld(cfg))
return error
