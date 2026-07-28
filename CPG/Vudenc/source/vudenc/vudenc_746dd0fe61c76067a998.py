def _ServerCleanup(self):...
if self._IsServerAlive():
self._server_popen.terminate()
utils.RemoveIfExists(self._temp_options_filename)
