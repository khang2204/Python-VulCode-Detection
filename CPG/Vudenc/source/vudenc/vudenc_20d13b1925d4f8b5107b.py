def check_origin(self):...
if log_check_output(['git', 'config', '--get', 'remote.origin.url']
if not self.has_local_edit():
logger.warning(
    "%s is not a clone of %s but it hasn't local modifications, removing it..",
    self.directory, self.url.geturl())
rmtree(self.directory)
self.checkout()
