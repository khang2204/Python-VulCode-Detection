def show_backends(serv, **kwargs):...
import json
import sql
haproxy_sock_port = sql.get_setting('haproxy_sock_port')
cmd = 'echo "show backend" |nc %s %s' % (serv, haproxy_sock_port)
output, stderr = subprocess_execute(cmd)
ret = ''
for line in output:
if '#' in line or 'stats' in line:
if kwargs.get('ret'):
if line != '':
return ret
back = json.dumps(line).split('"')
if kwargs.get('ret'):
ret += back[1]
print(back[1], end='<br>')
ret += '<br />'
