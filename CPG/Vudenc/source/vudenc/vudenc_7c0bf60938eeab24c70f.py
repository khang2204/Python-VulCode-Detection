def reset_dut(self, expected_output, attempts):...
if self.telnet:
for attempt in range(attempts):
self.dut.serial.write('\x03')
self.command('reset', expected_output, 'Error resetting DUT', False)
db.log_event('Warning' if attempt < attempts - 1 else 'Error', 'Debugger',
    'Error resetting DUT', db.log_exception)
db.log_event('Information', 'Debugger', 'Reset DUT')
print(colored(self.dut.serial.port + ': Error resetting DUT (attempt ' +
    str(attempt + 1) + '/' + str(attempts) + ')', 'red'))
if attempt < attempts - 1:
sleep(30)
