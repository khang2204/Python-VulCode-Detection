def __init__(self, addr=None, port=8888, breakpoints=None, connecttimeout=1.0):...
super(_LifecycleClient, self).__init__()
self._addr = Address.from_raw(addr, defaultport=port)
self._connecttimeout = connecttimeout
self._adapter = None
self._session = None
self._breakpoints = breakpoints
