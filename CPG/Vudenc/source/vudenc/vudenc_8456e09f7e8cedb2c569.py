import cgi
import os
import http.cookies
import funct
import sql
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates/'))
template = env.get_template('config.html')
print('Content-type: text/html\n')
funct.check_login()
form = cgi.FieldStorage()
serv = form.getvalue('serv')
config_read = ''
cfg = ''
stderr = ''
error = ''
aftersave = ''
cookie = http.cookies.SimpleCookie(os.environ.get('HTTP_COOKIE'))
hap_configs_dir = funct.get_config_var('configs', 'haproxy_save_configs_dir')
user_id = cookie.get('uuid')
if serv is not None:
user = sql.get_user_name_by_uuid(user_id.value)
cfg = hap_configs_dir + serv + '-' + funct.get_data('config') + '.cfg'
if serv is not None and form.getvalue('open') is not None:
servers = sql.get_dick_permit()
if serv is not None and form.getvalue('config') is not None:
funct.logging(serv, 'config.py open config')
error = funct.get_config(serv, cfg)
token = sql.get_token(user_id.value)
template = template.render(h2=1, title='Working with HAProxy configs', role
    =role, action='config.py', user=user, select_id='serv', serv=serv,
    aftersave=aftersave, config=config_read, cfg=cfg, selects=servers,
    stderr=stderr, error=error, note=1, token=token)
funct.logging(serv, 'config.py edited config')
config = form.getvalue('config')
conf = open(cfg, 'r')
error += "<br />Can't read import config file"
os.system('/bin/mv %s %s.old' % (cfg, cfg))
role = sql.get_user_role_by_uuid(user_id.value)
print(template)
oldcfg = form.getvalue('oldconfig')
config_read = conf.read()
save = form.getvalue('save')
conf.close
aftersave = 1
conf.write(config)
error = "Can't read import config file"
MASTERS = sql.is_master(serv)
for master in MASTERS:
if master[0] != None:
stderr = funct.upload_and_restart(serv, cfg, just_save=save)
funct.upload_and_restart(master[0], cfg, just_save=save)
funct.diff_config(oldcfg, cfg)
os.system('/bin/rm -f ' + hap_configs_dir + '*.old')
