def init(self):...
if not self.config:
self.logger.error(' Config not loaded yet!')
if not self.session:
self.logger.error(' Init aborted. No session was found!')
self.logger.debug(self.config)
window = find_window(self.session, self.window_name)
if window:
self.logger.debug("window '%s' found running" % self.window_name)
if not self.kill_mode:
if self.kill_mode:
self.logger.info("creating window '%s'" % self.window_name)
self.logger.info(
    "There is no component running by the name '%s'. Exiting kill mode" %
    self.window_name)
self.logger.info('Shutting down window...')
window = self.session.new_window(self.window_name)
kill_window(window)
start_window(window, self.config['cmd'][0]['start'], self.log_file, self.
    window_name)
self.logger.info('... done!')
