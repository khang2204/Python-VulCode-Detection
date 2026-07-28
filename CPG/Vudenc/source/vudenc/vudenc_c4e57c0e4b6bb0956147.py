def scan_targets_loop(self):...
while len(self.targets) == 0:
c = self.get_targets()
self.schedule(self.comment_loop)
if c == 0:
if len(self.forums) == 0:
self.log.info('No targets found at all, sleeping for 30 seconds')
self.schedule(self.wait_loop)
self.long_sleep(30)
