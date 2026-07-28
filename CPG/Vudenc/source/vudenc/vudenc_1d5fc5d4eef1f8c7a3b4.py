def syn_flood_protect(serv, **kwargs):...
import sql
script = 'syn_flood_protect.sh'
tmp_config_path = sql.get_setting('tmp_config_path')
enable = 'disable' if kwargs.get('enable') == '0' else 'disable'
os.system('cp scripts/%s .' % script)
commands = ['sudo chmod +x ' + tmp_config_path + script, tmp_config_path +
    script + ' ' + enable]
error = str(upload(serv, tmp_config_path, script))
if error:
print('error: ' + error)
os.system('rm -f %s' % script)
ssh_command(serv, commands, print_out='1')
