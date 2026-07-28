def start_component_without_deps(self, comp):...
if comp['host'] != 'localhost' and not self.run_on_localhost(comp):
self.logger.debug("Starting remote component '%s' on host '%s'" % (comp[
    'name'], comp['host']))
log_file = '%s/%s' % (TMP_LOG_PATH, comp['name'])
self.start_remote_component(comp['name'], comp['host'])
window = find_window(self.session, comp['name'])
if window:
self.logger.debug("Restarting '%s' in old window" % comp['name'])
self.logger.info("creating window '%s'" % comp['name'])
start_window(window, comp['cmd'][0]['start'], log_file, comp['name'])
window = self.session.new_window(comp['name'])
start_window(window, comp['cmd'][0]['start'], log_file, comp['name'])
