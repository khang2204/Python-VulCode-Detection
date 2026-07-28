def continue_dut(self, continue_command):...
self.command(continue_command, error_message='Error continuing DUT',
    log_event=False)
db.log_event('Information', 'Debugger', 'Continue DUT')
