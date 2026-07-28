def init(self):...
if not self.testing:
while True:
self.create_analysis_threads()
LOG.info('About to create analyziz threads')
self.create_analysis_threads()
LOG.info('just finished with analysis threads')
time.sleep(constants.SLEEP_TIME)
LOG.info('Just finished sleeping')
