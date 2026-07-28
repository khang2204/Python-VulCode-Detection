def connect(self, uid=UNKNOWN_UID, cmd=JsonRpcCommand.INIT):...
"""docstring"""
self._counter = self._id_counter()
self._conn = socket.create_connection(('127.0.0.1', self.host_port),
    _SOCKET_CONNECTION_TIMEOUT)
self._conn.settimeout(_SOCKET_READ_TIMEOUT)
self._client = self._conn.makefile(mode='brw')
resp = self._cmd(cmd, uid)
if not resp:
result = json.loads(str(resp, encoding='utf8'))
if result['status']:
self.uid = result['uid']
self.uid = UNKNOWN_UID
