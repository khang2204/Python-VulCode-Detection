async def push(self, item):...
if isinstance(item, FrameNavigated):
await self._runon('load')
self._loaded = True
