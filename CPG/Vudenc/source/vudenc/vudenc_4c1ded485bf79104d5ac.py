def run_check(self):...
if not self.config:
self.logger.error(' Config not loaded yet!')
if not self.session:
exit(CheckState.STOPPED.value)
self.logger.error(' Init aborted. No session was found!')
check_state = check_component(self.config, self.session, self.logger)
exit(CheckState.STOPPED.value)
exit(check_state.value)
