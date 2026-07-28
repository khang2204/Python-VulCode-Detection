async def fetch(self, entry, seqnum):...
"""docstring"""
assert isinstance(entry, SetEntry)
url = entry.value
depth = entry.depth
logger = self.logger.bind(url=url)
def formatCommand(e):...
if e.startswith('!'):
return e[1:]
return e.format(url=url, dest=dest.name)
