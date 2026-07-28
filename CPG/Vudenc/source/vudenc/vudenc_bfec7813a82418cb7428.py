async def push(self, item):...
if isinstance(item, ExtractLinksEvent):
it = iter(item.links)
limit = 100
while True:
limitlinks = list(islice(it, 0, limit))
if not limitlinks:
self.logger.info('extracted links', context=type(item).__name__, uuid=
    '8ee5e9c9-1130-4c5c-88ff-718508546e0c', links=limitlinks)
