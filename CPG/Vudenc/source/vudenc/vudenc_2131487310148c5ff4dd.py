async def run(self):...
logger = self.logger
async def processQueue():...
await self.processItem(item)
idle = IdleStateTracker(asyncio.get_event_loop())
self.handler.append(idle)
behavior = InjectBehaviorOnload(self)
self.handler.append(behavior)
handle = asyncio.ensure_future(processQueue())
timeoutProc = asyncio.ensure_future(asyncio.sleep(self.settings.timeout))
tab = l.tab
await tab.Security.setIgnoreCertificateErrors(ignore=self.settings.insecure)
self._enabledBehavior = list(filter(lambda x: self.url in x, map(lambda x:
    x(l, logger), self.behavior)))
version = await tab.Browser.getVersion()
payload = {'software': getSoftwareInfo(), 'browser': {'product': version[
    'product'], 'useragent': version['userAgent'], 'viewport': await
    getFormattedViewportMetrics(tab)}, 'tool': 'crocoite-single',
    'parameters': {'url': self.url, 'idleTimeout': self.settings.
    idleTimeout, 'timeout': self.settings.timeout, 'behavior': list(map(
    attrgetter('name'), self._enabledBehavior)), 'insecure': self.settings.
    insecure}}
if self.warcinfo:
payload['extra'] = self.warcinfo
await self.processItem(ControllerStart(payload))
await l.navigate(self.url)
idleProc = asyncio.ensure_future(idle.wait(self.settings.idleTimeout))
while True:
finished, pending = await asyncio.wait([idleProc, timeoutProc, handle],
    return_when=asyncio.FIRST_COMPLETED)
idleProc.cancel()
if handle in finished:
timeoutProc.cancel()
logger.error('fetch failed', uuid='43a0686a-a3a9-4214-9acd-43f6976f8ff3')
if timeoutProc in finished:
await behavior.stop()
idleProc.cancel()
logger.debug('global timeout', uuid='2f858adc-9448-4ace-94b4-7cd1484c0728')
if idleProc in finished:
await tab.Page.stopLoading()
timeoutProc.cancel()
idleProc.cancel()
logger.debug('idle timeout', uuid='90702590-94c4-44ef-9b37-02a16de444c3')
await asyncio.sleep(1)
handle.result()
timeoutProc.result()
idleProc.result()
await behavior.finish()
assert False
timeoutProc.cancel()
await asyncio.wait_for(idle.wait(1), timeout=1)
if handle.done():
handle.result()
handle.cancel()
