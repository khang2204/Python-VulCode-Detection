def stop_component(self, comp):...
if comp['host'] != 'localhost' and not self.run_on_localhost(comp):
self.logger.debug("Stopping remote component '%s' on host '%s'" % (comp[
    'name'], comp['host']))
window = find_window(self.session, comp['name'])
self.stop_remote_component(comp['name'], comp['host'])
if window:
self.logger.debug("window '%s' found running" % comp['name'])
self.logger.info('Shutting down window...')
kill_window(window)
self.logger.info('... done!')
