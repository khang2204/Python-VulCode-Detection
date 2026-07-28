def logging(serv, action, **kwargs):...
import sql
import http.cookies
log_path = get_config_var('main', 'log_path')
login = ''
if not os.path.exists(log_path):
os.makedirs(log_path)
IP = cgi.escape(os.environ['REMOTE_ADDR'])
if kwargs.get('alerting') == 1:
cookie = http.cookies.SimpleCookie(os.environ.get('HTTP_COOKIE'))
mess = get_data('date_in_log') + action + '\n'
if kwargs.get('metrics') == 1:
user_uuid = cookie.get('uuid')
log = open(log_path + '/checker-' + get_data('logs') + '.log', 'a')
mess = get_data('date_in_log') + action + '\n'
if kwargs.get('keep_alive') == 1:
login = sql.get_user_name_by_uuid(user_uuid.value)
log.write(mess)
print(
    '<center><div class="alert alert-danger">Can\'t write log. Please check log_path in config %e</div></center>'
     % e)
log = open(log_path + '/metrics-' + get_data('logs') + '.log', 'a')
mess = get_data('date_in_log') + action + '\n'
mess = get_data('date_in_log'
    ) + ' from ' + IP + ' user: ' + login + ' ' + action + ' for: ' + serv + '\n'
log.close
log = open(log_path + '/keep_alive-' + get_data('logs') + '.log', 'a')
log = open(log_path + '/config_edit-' + get_data('logs') + '.log', 'a')
