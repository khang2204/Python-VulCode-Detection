def wait():...
t.join(timeout=self._connecttimeout)
if t.is_alive():
warnings.warn('timed out waiting for connection')
if self._session is None:
message = 'unable to connect after {} secs'.format(self._connecttimeout)
if self._run_server_ex is None:
message = message + os.linesep + self._run_server_ex
