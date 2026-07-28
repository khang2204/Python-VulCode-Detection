def subproc_map(self, f, items):...
"""docstring"""
res = SubprocPool.foreground().map_async(f, items)
SubprocPool.shutdown(True)
while not res.ready():
res.wait(60)
return res.get()
if not res.ready():
self.log.debug('subproc_map result still not ready...')
