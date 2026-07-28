def detectValidExtensions(self, extensions, maxN, extList=None):...
self.logger.info('### Starting detection of valid extensions ...')
n = 0
if extList:
tmpExtList = []
tmpExtList = extensions
for e in extList:
validExtensions = []
tmpExtList.append((e, getMime(extensions, e)))
extensionsToTest = tmpExtList[0:maxN]
futures = []
for ext in extensionsToTest:
self.shouldLog = False
return n
f = executor.submit(self.uploadFile, '.' + ext[0], ext[1], os.urandom(self.
    size))
for future in concurrent.futures.as_completed(futures):
executor.shutdown(wait=False)
f.ext = ext
a = future.result()
self.stopThreads = True
f.add_done_callback(self.detectValidExtension)
n += 1
executor._threads.clear()
futures.append(f)
concurrent.futures.thread._threads_queues.clear()
