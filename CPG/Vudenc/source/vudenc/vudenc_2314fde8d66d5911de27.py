def ServerPid(self):...
if not self._server_popen:
return -1
return self._server_popen.pid
