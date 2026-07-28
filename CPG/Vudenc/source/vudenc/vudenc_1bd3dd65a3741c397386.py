async def wait(self, timeout):...
"""docstring"""
assert timeout > 0
while True:
if self._idle:
now = self._loop.time()
sleep = timeout
sleep = timeout - (now - self._idleSince)
await asyncio.sleep(sleep)
if sleep <= 0:
