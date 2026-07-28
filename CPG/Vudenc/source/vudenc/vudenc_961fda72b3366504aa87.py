def update(self):...
if not exists(self.directory):
self.checkout()
if not exists(self.directory + '/.git'):
not_a_project(self.directory, 'Git')
if self.has_local_edit():
logger.warning("Directory '%s' contains local modifications" % self.directory)
if self.conf.get('shallow', False):
fork(['git', 'fetch', '--depth', '1', 'origin', self.noremote_ref()])
fork(['git', 'fetch'])
fork(['git', 'checkout', 'FETCH_HEAD', '--'])
fork(['git', 'checkout', self.ref, '--'])
