def __init__(self, debug=False, one_shot=False):...
"""docstring"""
RESTClient.__init__(self, 'workqueue')
conf = getConfig('worker')
self._uid = uuid.uuid4()
Daemon.__init__(self, pidfile='/tmp/worker-%s.pid' % self._uid, logfile=
    '/tmp/worker-%s.log' % self._uid, target=self.run, debug=debug)
self._one_shot = one_shot
self._types = [JobType[type_.upper()] for type_ in conf.pop('types', (
    'LIST', 'COPY', 'REMOVE'))]
self._interpoll_sleep_time = conf.pop('poll_time', 2)
self._script_path = conf.pop('script_path', None)
if self._script_path:
self._script_path = os.path.abspath(self._script_path)
code_path = os.path.abspath(os.path.dirname(__file__))
self._logger.info('Script search path is: %s', self._script_path)
self._script_path = os.path.join(code_path, 'scripts')
self._current_process = None
if conf:
keys = ', '.join(conf.keys())
