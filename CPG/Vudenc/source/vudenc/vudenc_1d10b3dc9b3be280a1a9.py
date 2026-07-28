def __init__(self, conn, seq=1000, handlers=(), timeout=None, owned=False):...
super(DebugSession, self).__init__()
self._conn = conn
self._seq = seq
self._timeout = timeout
self._owned = owned
self._handlers = []
for handler in handlers:
if callable(handler):
self._received = []
self._add_handler(handler)
self._add_handler(*handler)
self._listenerthread = new_hidden_thread(target=self._listen, name=
    'test.session')
self._listenerthread.start()
