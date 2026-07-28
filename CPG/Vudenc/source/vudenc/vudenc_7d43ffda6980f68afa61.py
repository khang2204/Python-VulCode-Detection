async def run(self):...
def log():...
self.logger.info('recursing', uuid='5b8498e4-868d-413c-a67e-004516b8452c',
    pending=len(self.pending), have=len(self.have) - len(self.running),
    running=len(self.running))
seqnum = 1
self.have = set()
self.logger.info('cancel', uuid='d58154c8-ec27-40f2-ab9e-e25c1b21cd88',
    pending=len(self.pending), have=len(self.have) - len(self.running),
    running=len(self.running))
done = await asyncio.gather(*self.running, return_exceptions=True)
self.pending = set([SetEntry(self.url, depth=0)])
for r in done:
while self.pending:
if isinstance(r, Exception):
self.running = set()
u = self.pending.pop()
log()
self.have.add(u)
t = asyncio.ensure_future(self.fetch(u, seqnum))
self.running.add(t)
seqnum += 1
log()
if len(self.running) >= self.concurrency or not self.pending:
done, pending = await asyncio.wait(self.running, return_when=asyncio.
    FIRST_COMPLETED)
self.running.difference_update(done)
for r in done:
r.result()
