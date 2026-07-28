def __init__(self, sock, ownsock=False):...
super(DebugSessionConnection, self).__init__()
self._sock = sock
self._ownsock = ownsock
