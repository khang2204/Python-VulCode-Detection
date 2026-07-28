def __init__(self, loop):...
self._idle = True
self._loop = loop
self._idleSince = self._loop.time()
