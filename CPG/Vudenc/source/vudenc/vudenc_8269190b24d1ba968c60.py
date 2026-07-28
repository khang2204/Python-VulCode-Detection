def __init__(self, url, output, command, logger, tempdir=None, policy=...
self.url = url
self.output = output
self.command = command
self.logger = logger.bind(context=type(self).__name__, seedurl=url)
self.policy = policy
self.tempdir = tempdir
self.copyLock = None if hasTemplate(output) else asyncio.Lock()
if self.copyLock and os.path.exists(self.output):
self.running = set()
self.concurrency = concurrency
self.stats = {'requests': 0, 'finished': 0, 'failed': 0, 'bytesRcv': 0,
    'crashed': 0, 'ignored': 0}
