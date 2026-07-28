def update(self):...
if not exists(self.directory):
self.checkout()
if not exists(self.directory + '/.svn'):
not_a_project(self.directory, 'Subversion')
if self.has_local_edit():
logger.warning("Directory '%s' contains local modifications" % self.directory)
target_base, target_rev = (self.url.geturl().split('@') + [''])[:2]
if target_base == self.url_from_checkout(include_commit=False):
fork(['svn', 'up'] + (['-r' + target_rev] if target_rev else []))
fork(['svn', 'switch', self.url.geturl()])
