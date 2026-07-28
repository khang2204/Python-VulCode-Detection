def host_local_debugger(self, argv, script=None, env=None, cwd=None, **kwargs):...
if self.closed:
if self._adapter is not None:
assert self._session is None
addr = 'localhost', self._addr.port
self._run_server_ex = None
def run():...
self._session = self.SESSION.create_server(addr, **kwargs)
self._run_server_ex = traceback.format_exc()
t = new_hidden_thread(target=run, name='test.client')
t.start()
def wait():...
t.join(timeout=self._connecttimeout)
if t.is_alive():
warnings.warn('timed out waiting for connection')
if self._session is None:
message = 'unable to connect after {} secs'.format(self._connecttimeout)
self._launch(argv, script=script, wait_for_connect=wait, detachable=False,
    env=env, cwd=cwd)
if self._run_server_ex is None:
return self._adapter, self._session
message = message + os.linesep + self._run_server_ex
