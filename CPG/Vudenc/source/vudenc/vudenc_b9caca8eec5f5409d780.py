def __init__(self):...
self.connect()
signal.signal(signal.SIGTERM, self.exit)
log.info('Worker starting')
