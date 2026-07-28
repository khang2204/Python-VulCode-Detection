import cgi
import os, sys
import funct
import sql
import ovw
form = cgi.FieldStorage()
serv = form.getvalue('serv')
act = form.getvalue('act')
print('Content-type: text/html\n')
if act == 'checkrestart':
servers = sql.get_dick_permit(ip=serv)
if form.getvalue('token') is None:
for server in servers:
print('What the fuck?! U r hacker Oo?!')
if form.getvalue('getcerts') is not None and serv is not None:
if server != '':
sys.exit()
sys.exit()
cert_path = sql.get_setting('cert_path')
if form.getvalue('checkSshConnect') is not None and serv is not None:
print('ok')
commands = ['ls -1t ' + cert_path + ' |grep pem']
if form.getvalue('getcert') is not None and serv is not None:
funct.ssh_command(serv, ['ls -1t'])
print(
    '<div class="alert alert-danger" style="margin:0">Can not connect to the server</div>'
    )
sys.exit()
funct.ssh_command(serv, commands, ip='1')
print(
    '<div class="alert alert-danger" style="margin:0">Can not connect to the server</div>'
    )
id = form.getvalue('getcert')
if form.getvalue('ssh_cert'):
cert_path = sql.get_setting('cert_path')
name = form.getvalue('name')
if serv and form.getvalue('ssl_cert'):
commands = ['cat ' + cert_path + '/' + id]
if not os.path.exists(os.getcwd() + '/keys/'):
cert_local_dir = funct.get_config_var('main', 'cert_local_dir')
if form.getvalue('backend') is not None:
funct.ssh_command(serv, commands, ip='1')
print(
    '<div class="alert alert-danger" style="margin:0">Can not connect to the server</div>'
    )
os.makedirs(os.getcwd() + '/keys/')
ssh_keys = os.path.dirname(os.getcwd()) + '/keys/' + name + '.pem'
cert_path = sql.get_setting('cert_path')
funct.show_backends(serv)
if form.getvalue('ip') is not None and serv is not None:
conf.write(form.getvalue('ssh_cert'))
print(
    '<div class="alert alert-danger">Can\'t save ssh keys file. Check ssh keys path in config</div>'
    )
print('<div class="alert alert-success">Ssh key was save into: %s </div>' %
    ssh_keys)
if not os.path.exists(cert_local_dir):
commands = [
    "sudo ip a |grep inet |egrep -v  '::1' |awk '{ print $2  }' |awk -F'/' '{ print $1  }'"
    ]
if form.getvalue('showif'):
funct.logging('local', 'users.py#ssh upload new ssh cert %s' % ssh_keys)
os.makedirs(cert_local_dir)
if form.getvalue('ssl_name') is None:
funct.ssh_command(serv, commands, ip='1')
commands = [
    "sudo ip link|grep 'UP' | awk '{print $2}'  |awk -F':' '{print $1}'"]
if form.getvalue('action_hap') is not None and serv is not None:
print('<div class="alert alert-danger">Please enter desired name</div>')
name = form.getvalue('ssl_name') + '.pem'
funct.ssh_command(serv, commands, ip='1')
action = form.getvalue('action_hap')
if form.getvalue('action_waf') is not None and serv is not None:
ssl_cert.write(form.getvalue('ssl_cert'))
print(
    '<div class="alert alert-danger">Can\'t save ssl keys file. Check ssh keys path in config</div>'
    )
print(
    '<div class="alert alert-success">SSL file was upload to %s into: %s </div>'
     % (serv, cert_path))
if funct.check_haproxy_config(serv):
serv = form.getvalue('serv')
if act == 'overview':
MASTERS = sql.is_master(serv)
commands = ['sudo systemctl %s haproxy' % action]
print('Bad config, check please')
action = form.getvalue('action_waf')
ovw.get_overview()
if act == 'overviewwaf':
for master in MASTERS:
funct.ssh_command(serv, commands)
commands = ['sudo systemctl %s waf' % action]
ovw.get_overviewWaf(form.getvalue('page'))
if act == 'overviewServers':
if master[0] != None:
funct.upload(serv, cert_path, name)
os.system('mv %s %s' % (name, cert_local_dir))
print('HAproxy was %s' % action)
funct.ssh_command(serv, commands)
ovw.get_overviewServers()
if form.getvalue('action'):
funct.upload(master[0], cert_path, name)
funct.logging(serv, 'add.py#ssl upload new ssl cert %s' % name)
import requests
if serv is not None and act == 'stats':
from requests_toolbelt.utils import dump
import requests
if serv is not None and form.getvalue('rows') is not None:
haproxy_user = sql.get_setting('stats_user')
from requests_toolbelt.utils import dump
rows = form.getvalue('rows')
if serv is not None and form.getvalue('rows1') is not None:
haproxy_pass = sql.get_setting('stats_password')
haproxy_user = sql.get_setting('stats_user')
waf = form.getvalue('waf')
rows = form.getvalue('rows1')
if form.getvalue('viewlogs') is not None:
stats_port = sql.get_setting('stats_port')
haproxy_pass = sql.get_setting('stats_password')
grep = form.getvalue('grep')
grep = form.getvalue('grep')
viewlog = form.getvalue('viewlogs')
if serv is not None and act == 'showMap':
stats_page = sql.get_setting('stats_page')
stats_port = sql.get_setting('stats_port')
hour = form.getvalue('hour')
hour = form.getvalue('hour')
log_path = funct.get_config_var('main', 'log_path')
ovw.get_map(serv)
if form.getvalue('servaction') is not None:
postdata = {'action': form.getvalue('action'), 's': form.getvalue('s'), 'b':
    form.getvalue('b')}
stats_page = sql.get_setting('stats_page')
minut = form.getvalue('minut')
minut = form.getvalue('minut')
rows = form.getvalue('rows2')
server_state_file = sql.get_setting('server_state_file')
if act == 'showCompareConfigs':
headers = {'User-Agent':
    'Mozilla/5.0 (Windows NT 5.1; rv:20.0) Gecko/20100101 Firefox/20.0',
    'Accept':
    'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5', 'Accept-Encoding': 'gzip, deflate'}
response = requests.get('http://%s:%s/%s' % (serv, stats_port, stats_page),
    auth=(haproxy_user, haproxy_pass))
print('Oops. Connection timeout occured!')
data = response.content
hour1 = form.getvalue('hour1')
hour1 = form.getvalue('hour1')
grep = form.getvalue('grep')
haproxy_sock = sql.get_setting('haproxy_sock')
import glob
if serv is not None and form.getvalue('right') is not None:
q = requests.post('http://' + serv + ':' + stats_port + '/' + stats_page,
    headers=headers, data=postdata, auth=(haproxy_user, haproxy_pass))
print('Oops. Read timeout occured')
print(data.decode('utf-8'))
minut1 = form.getvalue('minut1')
minut1 = form.getvalue('minut1')
hour = form.getvalue('hour')
enable = form.getvalue('servaction')
from jinja2 import Environment, FileSystemLoader
from jinja2 import Environment, FileSystemLoader
if serv is not None and act == 'configShow':
print('Http Error:', errh)
date = hour + ':' + minut
date = hour + ':' + minut
minut = form.getvalue('minut')
backend = form.getvalue('servbackend')
env = Environment(loader=FileSystemLoader('templates/ajax'))
left = form.getvalue('left')
hap_configs_dir = funct.get_config_var('configs', 'haproxy_save_configs_dir')
if form.getvalue('master'):
print('<div class="alert alert-danger">Error Connecting: %s</div>' % errc)
date1 = hour1 + ':' + minut1
date1 = hour1 + ':' + minut1
hour1 = form.getvalue('hour1')
cmd = (
    'echo "%s %s" |sudo socat stdio %s | cut -d "," -f 1-2,5-10,18,34-36 | column -s, -t'
     % (enable, backend, haproxy_sock))
template = env.get_template('/show_compare_configs.html')
right = form.getvalue('right')
if form.getvalue('configver') is None:
master = form.getvalue('master')
if form.getvalue('masteradd'):
print('Timeout Error:', errt)
if grep is not None:
apache_log_path = sql.get_setting('apache_log_path')
minut1 = form.getvalue('minut1')
if form.getvalue('save') == 'on':
left = form.getvalue('left')
hap_configs_dir = funct.get_config_var('configs', 'haproxy_save_configs_dir')
cfg = hap_configs_dir + serv + '-' + funct.get_data('config') + '.cfg'
cfg = hap_configs_dir + form.getvalue('configver')
slave = form.getvalue('slave')
master = form.getvalue('masteradd')
if form.getvalue('haproxyaddserv'):
print('OOps: Something Else', err)
grep_act = '|grep'
grep_act = ''
if grep is not None:
date = hour + ':' + minut
save_command = 'echo "show servers state" | sudo socat stdio %s > %s' % (
    haproxy_sock, server_state_file)
command = [cmd]
right = form.getvalue('right')
cmd = 'diff -ub %s%s %s%s' % (hap_configs_dir, left, hap_configs_dir, right)
funct.get_config(serv, cfg)
conf = open(cfg, 'r')
print('<div class="alert alert-danger">Can\'t read import config file</div>')
from jinja2 import Environment, FileSystemLoader
interface = form.getvalue('interface')
slave = form.getvalue('slaveadd')
funct.install_haproxy(form.getvalue('haproxyaddserv'), syn_flood=form.
    getvalue('syn_flood'))
if form.getvalue('installwaf'):
syslog_server_enable = sql.get_setting('syslog_server_enable')
grep = ''
grep_act = '|grep'
grep_act = ''
date1 = hour1 + ':' + minut1
command = [cmd, save_command]
if enable != 'show':
template = template.render(serv=serv, right=right, left=left, return_files=
    funct.get_files())
env = Environment(loader=FileSystemLoader('templates/ajax'), extensions=[
    'jinja2.ext.loopcontrols', 'jinja2.ext.do'])
env = Environment(loader=FileSystemLoader('templates/ajax'), extensions=[
    'jinja2.ext.loopcontrols'])
vrrpip = form.getvalue('vrrpip')
interface = form.getvalue('interfaceadd')
funct.waf_install(form.getvalue('installwaf'))
if form.getvalue('metrics_waf'):
if syslog_server_enable is None or syslog_server_enable == '0':
if serv == 'haproxy-wi.access.log':
grep = ''
if grep is not None:
print(
    '<center><h3>You %s %s on HAproxy %s. <a href="viewsttats.py?serv=%s" title="View stat" target="_blank">Look it</a> or <a href="edit.py" title="Edit">Edit something else</a></h3><br />'
     % (enable, backend, serv, serv))
funct.ssh_command(serv, command, show_log='1')
print(template)
template = env.get_template('compare.html')
template = env.get_template('config_show.html')
tmp_config_path = sql.get_setting('tmp_config_path')
vrrpip = form.getvalue('vrrpipadd')
sql.update_waf_metrics_enable(form.getvalue('metrics_waf'), form.getvalue(
    'enable'))
if form.getvalue('table_metrics'):
local_path_logs = sql.get_setting('local_path_logs')
commands = [
    "sudo cat /var/log/%s/syslog.log | sed '/ %s:00/,/ %s:00/! d' |tail -%s  %s %s"
     % (serv, date, date1, rows, grep_act, grep)]
cmd = 'cat %s| awk -F"/|:" \'$3>"%s:00" && $3<"%s:00"\' |tail -%s  %s %s' % (
    apache_log_path + '/' + serv, date, date1, rows, grep_act, grep)
cmd = 'cat %s| awk \'$4>"%s:00" && $4<"%s:00"\' |tail -%s  %s %s' % (
    apache_log_path + '/' + serv, date, date1, rows, grep_act, grep)
grep_act = '|grep'
grep_act = ''
action = 'edit.py ' + enable + ' ' + backend
output, stderr = funct.subprocess_execute(cmd)
template = template.render(conf=conf, view=form.getvalue('view'), serv=serv,
    configver=form.getvalue('configver'), role=funct.is_admin(level=2))
script = 'install_keepalived.sh'
kp = form.getvalue('kp')
import http.cookies
if form.getvalue('metrics'):
syslog_server = serv
syslog_server = sql.get_setting('syslog_server')
output, stderr = funct.subprocess_execute(cmd)
cmd = 'cat %s| awk \'$3>"%s:00" && $3<"%s:00"\' |tail -%s  %s %s' % (
    log_path + viewlog, date, date1, rows, grep_act, grep)
grep = ''
funct.logging(serv, action)
template = template.render(stdout=output)
print(template)
if form.getvalue('hap') == '1':
tmp_config_path = sql.get_setting('tmp_config_path')
from jinja2 import Environment, FileSystemLoader
from datetime import timedelta
if form.getvalue('waf_metrics'):
commands = [
    'sudo cat %s| awk \'$3>"%s:00" && $3<"%s:00"\' |tail -%s  %s %s' % (
    local_path_logs, date, date1, rows, grep_act, grep)]
if waf == '1':
funct.show_log(output)
output, stderr = funct.subprocess_execute(cmd)
print(template)
if form.getvalue('configver') is None:
funct.install_haproxy(master)
if form.getvalue('syn_flood') == '1':
script = 'add_vrrp.sh'
env = Environment(loader=FileSystemLoader('templates/ajax'))
from bokeh.plotting import figure, output_file, show
from datetime import timedelta
if form.getvalue('get_hap_v'):
local_path_logs = '/var/log/modsec_audit.log'
funct.ssh_command(syslog_server, commands, show_log='1')
print(stderr)
funct.show_log(output)
print(stderr)
os.system('/bin/rm -f ' + cfg)
funct.install_haproxy(slave)
funct.syn_flood_protect(master)
os.system('cp scripts/%s .' % script)
os.system('cp scripts/%s .' % script)
template = env.get_template('table_metrics.html')
from bokeh.models import ColumnDataSource, HoverTool, DatetimeTickFormatter, DatePicker
from bokeh.plotting import figure, output_file, show
output = funct.check_haproxy_version(serv)
if form.getvalue('bwlists'):
commands = ['sudo cat %s |tail -%s  %s %s' % (local_path_logs, rows,
    grep_act, grep)]
print(stderr)
funct.syn_flood_protect(slave)
error = str(funct.upload(master, tmp_config_path, script))
error = str(funct.upload(master, tmp_config_path, script))
cookie = http.cookies.SimpleCookie(os.environ.get('HTTP_COOKIE'))
from bokeh.layouts import widgetbox, gridplot
from bokeh.models import ColumnDataSource, HoverTool, DatetimeTickFormatter, DatePicker
print(output)
list = os.path.dirname(os.getcwd()) + '/' + sql.get_setting('lists_path'
    ) + '/' + form.getvalue('group') + '/' + form.getvalue('color'
    ) + '/' + form.getvalue('bwlists')
if form.getvalue('bwlists_create'):
if error:
if error:
user_id = cookie.get('uuid')
from bokeh.models.widgets import Button, RadioButtonGroup, Select
from bokeh.layouts import widgetbox, gridplot
file = open(list, 'r')
print('<div class="alert alert-danger" style="margin:0">Cat\'n read ' +
    form.getvalue('color') + ' list</div>')
list_name = form.getvalue('bwlists_create').split('.')[0]
if form.getvalue('bwlists_save'):
print('error: ' + error)
funct.upload(slave, tmp_config_path, script)
print('error: ' + error)
funct.upload(slave, tmp_config_path, script)
table_stat = sql.select_table_metrics(user_id.value)
import pandas as pd
from bokeh.models.widgets import Button, RadioButtonGroup, Select
file_read = file.read()
list_name += '.lst'
list = os.path.dirname(os.getcwd()) + '/' + sql.get_setting('lists_path'
    ) + '/' + form.getvalue('group') + '/' + form.getvalue('color'
    ) + '/' + form.getvalue('bwlists_save')
if form.getvalue('get_lists'):
sys.exit()
funct.ssh_command(master, ['sudo chmod +x ' + tmp_config_path + script, 
    tmp_config_path + script + ' MASTER ' + interface + ' ' + vrrpip])
sys.exit()
funct.ssh_command(master, ['sudo chmod +x ' + tmp_config_path + script, 
    tmp_config_path + script + ' MASTER ' + interface + ' ' + vrrpip + ' ' +
    kp])
template = template.render(table_stat=sql.select_table_metrics(user_id.value))
import http.cookies
import pandas as pd
file.close
list = os.path.dirname(os.getcwd()) + '/' + sql.get_setting('lists_path'
    ) + '/' + form.getvalue('group') + '/' + form.getvalue('color'
    ) + '/' + list_name
file.write(form.getvalue('bwlists_content'))
print('<div class="alert alert-danger" style="margin:0">Cat\'n save ' +
    form.getvalue('color') + ' list. %s </div>' % e)
servers = sql.get_dick_permit()
list = os.path.dirname(os.getcwd()) + '/' + sql.get_setting('lists_path'
    ) + '/' + form.getvalue('group') + '/' + form.getvalue('color')
if form.getvalue('get_ldap_email'):
funct.ssh_command(slave, ['sudo chmod +x ' + tmp_config_path + script, 
    tmp_config_path + script + ' BACKUP ' + interface + ' ' + vrrpip])
funct.ssh_command(slave, ['sudo chmod +x ' + tmp_config_path + script, 
    tmp_config_path + script + ' BACKUP ' + interface + ' ' + vrrpip + ' ' +
    kp])
print(template)
cookie = http.cookies.SimpleCookie(os.environ.get('HTTP_COOKIE'))
import http.cookies
print(file_read)
open(list, 'a').close()
print('<div class="alert alert-danger" style="margin:0">Cat\'n create new ' +
    form.getvalue('color') + ' list. %s </div>' % e)
path = sql.get_setting('haproxy_dir') + '/' + form.getvalue('color')
lists = funct.get_files(dir=list, format='lst')
username = form.getvalue('get_ldap_email')
os.system('rm -f %s' % script)
os.system('rm -f %s' % script)
user_id = cookie.get('uuid')
cookie = http.cookies.SimpleCookie(os.environ.get('HTTP_COOKIE'))
print('<div class="alert alert-success" style="margin:0">' + form.getvalue(
    'color') + ' list was created</div>')
for server in servers:
for list in lists:
import ldap
sql.update_server_master(master, slave)
servers = sql.select_servers_metrics(user_id.value)
user_id = cookie.get('uuid')
funct.ssh_command(server[2], ['sudo mkdir ' + path])
print(list)
server = sql.get_setting('ldap_server')
servers = sorted(servers)
servers = sql.select_waf_servers_metrics(user_id.value)
error = funct.upload(server[2], path + '/' + form.getvalue('bwlists_save'),
    list, dir='fullpath')
port = sql.get_setting('ldap_port')
p = {}
servers = sorted(servers)
if error:
user = sql.get_setting('ldap_user')
for serv in servers:
p = {}
print('<div class="alert alert-danger">Upload fail: %s</div>' % error)
print('<div class="alert alert-success" style="margin:10px">Edited ' + form
    .getvalue('color') + ' list was uploaded to ' + server[1] + '</div>')
password = sql.get_setting('ldap_password')
serv = serv[0]
plots = []
for serv in servers:
if form.getvalue('bwlists_restart') == 'restart':
ldap_base = sql.get_setting('ldap_base')
p[serv] = {}
for key, value in p.items():
serv = serv[0]
plots = []
funct.ssh_command(server[2], ['sudo ' + sql.get_setting('restart_command')])
domain = sql.get_setting('ldap_domain')
metric = sql.select_metrics(serv)
plots.append(value)
grid = gridplot(plots, ncols=2, plot_width=800, plot_height=250,
    toolbar_location='left', toolbar_options=dict(logo=None))
p[serv] = {}
for key, value in p.items():
ldap_search_field = sql.get_setting('ldap_search_field')
metrics = {}
show(grid)
metric = sql.select_waf_metrics(serv)
plots.append(value)
grid = gridplot(plots, ncols=2, plot_width=800, plot_height=250,
    toolbar_location='left', toolbar_options=dict(logo=None))
l = ldap.initialize('ldap://' + server + ':' + port)
for i in metric:
metrics = {}
show(grid)
l.protocol_version = ldap.VERSION3
l.unbind()
rep_date = str(i[5])
df = pd.DataFrame.from_dict(metrics, orient='index')
for i in metric:
l.set_option(ldap.OPT_REFERRALS, 0)
metrics[rep_date] = {}
df = df.fillna(0)
rep_date = str(i[2])
df = pd.DataFrame.from_dict(metrics, orient='index')
bind = l.simple_bind_s(user, password)
metrics[rep_date]['server'] = str(i[0])
df.index = pd.to_datetime(df.index)
metrics[rep_date] = {}
df = df.fillna(0)
criteria = '(&(objectClass=user)(sAMAccountName=' + username + '))'
metrics[rep_date]['curr_con'] = str(i[1])
df.index.name = 'Date'
metrics[rep_date]['conn'] = str(i[1])
df.index = pd.to_datetime(df.index)
attributes = [ldap_search_field]
metrics[rep_date]['curr_ssl_con'] = str(i[2])
df.sort_index(inplace=True)
df.index.name = 'Date'
result = l.search_s(ldap_base, ldap.SCOPE_SUBTREE, criteria, attributes)
metrics[rep_date]['sess_rate'] = str(i[3])
source = ColumnDataSource(df)
df.sort_index(inplace=True)
results = [entry for dn, entry in result if isinstance(entry, dict)]
metrics[rep_date]['max_sess_rate'] = str(i[4])
output_file('templates/metrics_out.html', mode='inline')
source = ColumnDataSource(df)
print('["' + results[0][ldap_search_field][0].decode('utf-8') + '","' +
    domain + '"]')
print('error: user not found')
x_min = df.index.min() - pd.Timedelta(hours=1)
output_file('templates/metrics_waf_out.html', mode='inline')
x_max = df.index.max() + pd.Timedelta(minutes=1)
x_min = df.index.min() - pd.Timedelta(hours=1)
p[serv] = figure(tools='pan,box_zoom,reset,xwheel_zoom', title=metric[0][0],
    x_axis_type='datetime', y_axis_label='Connections', x_range=(x_max.
    timestamp() * 1000 - 60 * 100000, x_max.timestamp() * 1000))
x_max = df.index.max() + pd.Timedelta(minutes=1)
hover = HoverTool(tooltips=[('Connections', '@curr_con'), (
    'SSL connections', '@curr_ssl_con'), ('Sessions rate', '@sess_rate')],
    mode='mouse')
p[serv] = figure(tools='pan,box_zoom,reset,xwheel_zoom', title=metric[0][0],
    x_axis_type='datetime', y_axis_label='Connections', x_range=(x_max.
    timestamp() * 1000 - 60 * 100000, x_max.timestamp() * 1000))
p[serv].ygrid.band_fill_color = '#f3f8fb'
hover = HoverTool(tooltips=[('Connections', '@conn')], mode='mouse')
p[serv].ygrid.band_fill_alpha = 0.9
p[serv].ygrid.band_fill_color = '#f3f8fb'
p[serv].y_range.start = 0
p[serv].ygrid.band_fill_alpha = 0.9
p[serv].y_range.end = int(df['curr_con'].max()) + 150
p[serv].y_range.start = 0
p[serv].add_tools(hover)
p[serv].y_range.end = int(df['conn'].max()) + 150
p[serv].title.text_font_size = '20px'
p[serv].add_tools(hover)
p[serv].line('Date', 'curr_con', source=source, alpha=0.5, color='#5cb85c',
    line_width=2, legend='Conn')
p[serv].title.text_font_size = '20px'
p[serv].line('Date', 'curr_ssl_con', source=source, alpha=0.5, color=
    '#5d9ceb', line_width=2, legend='SSL con')
p[serv].line('Date', 'conn', source=source, alpha=0.5, color='#5cb85c',
    line_width=2, legend='Conn')
p[serv].line('Date', 'sess_rate', source=source, alpha=0.5, color='#33414e',
    line_width=2, legend='Sessions')
p[serv].legend.orientation = 'horizontal'
p[serv].legend.orientation = 'horizontal'
p[serv].legend.location = 'top_left'
p[serv].legend.location = 'top_left'
p[serv].legend.padding = 5
p[serv].legend.padding = 5
