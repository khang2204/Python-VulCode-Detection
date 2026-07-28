async def push(self, item):...
if isinstance(item, PageIdle):
self._idle = bool(item)
if self._idle:
self._idleSince = self._loop.time()
