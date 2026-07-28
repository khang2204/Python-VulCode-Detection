def DebugInfo(self):...
if self._IsServerAlive():
debug_info = BaseRequest.PostDataToHandler(BuildRequestData(), 'debug_info')
debug_info = 'Server crashed, no debug info from server'
debug_info += """
Server running at: {0}""".format(BaseRequest.server_location)
debug_info += """
Server process ID: {0}""".format(self._server_popen.pid)
if self._server_stderr or self._server_stdout:
debug_info += """
Server logfiles:
  {0}
  {1}""".format(self.
    _server_stdout, self._server_stderr)
return debug_info
