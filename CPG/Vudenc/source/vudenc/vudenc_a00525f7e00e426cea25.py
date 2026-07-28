def _cmd(self, command, uid=None):...
"""docstring"""
if not uid:
uid = self.uid
self._client.write(json.dumps({'cmd': command, 'uid': uid}).encode('utf8') +
    b'\n')
self._client.flush()
return self._client.readline()
