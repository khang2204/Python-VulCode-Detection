def waf_install(serv, **kwargs):...
import sql
script = 'waf.sh'
tmp_config_path = sql.get_setting('tmp_config_path')
proxy = sql.get_setting('proxy')
haproxy_dir = sql.get_setting('haproxy_dir')
ver = check_haproxy_version(serv)
os.system('cp scripts/%s .' % script)
commands = ['sudo chmod +x ' + tmp_config_path + script + ' && ' +
    tmp_config_path + script + ' PROXY=' + proxy + ' HAPROXY_PATH=' +
    haproxy_dir + ' VERSION=' + ver]
error = str(upload(serv, tmp_config_path, script))
if error:
print('error: ' + error)
os.system('rm -f %s' % script)
stderr = ssh_command(serv, commands, print_out='1')
if stderr is None:
sql.insert_waf_metrics_enable(serv, '0')
