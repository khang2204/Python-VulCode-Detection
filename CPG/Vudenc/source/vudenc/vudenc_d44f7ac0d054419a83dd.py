def check_haproxy_version(serv):...
import sql
haproxy_sock_port = sql.get_setting('haproxy_sock_port')
ver = ''
cmd = "echo 'show info' |nc %s %s |grep Version |awk '{print $2}'" % (serv,
    haproxy_sock_port)
output, stderr = subprocess_execute(cmd)
for line in output:
ver = line
return ver
