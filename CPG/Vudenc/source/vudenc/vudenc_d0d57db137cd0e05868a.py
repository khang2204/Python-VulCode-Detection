async def push(self, item):...
if isinstance(item, RequestResponsePair):
self.stats['requests'] += 1
if not item.response:
self.stats['failed'] += 1
self.stats['finished'] += 1
self.stats['bytesRcv'] += item.response.bytesReceived
