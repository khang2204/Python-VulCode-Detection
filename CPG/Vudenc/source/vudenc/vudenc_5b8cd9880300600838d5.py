def __init__(self, configfile=None, kill_mode=False, check_mode=False):...
self.kill_mode = kill_mode
self.check_mode = check_mode
self.logger = logging.getLogger(__name__)
self.logger.setLevel(logging.DEBUG)
self.config = None
self.session = None
if kill_mode:
self.logger.info('started slave with kill mode')
if check_mode:
self.logger.info('started slave with check mode')
self.server = Server()
if self.server.has_session('slave-session'):
self.session = self.server.find_where({'session_name': 'slave-session'})
if not kill_mode and not check_mode:
self.logger.info('found running slave session on server')
self.logger.info('starting new slave session on server')
self.logger.info('No slave session found on server. Aborting')
if configfile:
self.session = self.server.new_session(session_name='slave-session')
exit(CheckState.STOPPED)
self.load_config(configfile)
self.logger.error('No slave component config provided')
self.window_name = self.config['name']
self.flag_path = '/tmp/Hyperion/slaves/%s' % self.window_name
self.log_file = '/tmp/Hyperion/log/%s' % self.window_name
ensure_dir(self.log_file)
