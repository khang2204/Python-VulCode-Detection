def command(self, command, expected_output, error_message, log_event,...
if log_event:
event = db.log_event('Information', 'Debugger', 'Command', command, success
    =False)
expected_output = [bytes(output, encoding='utf-8') for output in
    expected_output]
return_buffer = ''
if error_message is None:
error_message = command
buff = self.telnet.read_very_eager().decode('utf-8', 'replace')
if self.db.result:
self.db.result['debugger_output'] += buff
self.db.campaign['debugger_output'] += buff
if self.options.debug:
print(colored(buff, 'yellow'))
if command:
self.telnet.write(bytes(command + line_ending, encoding='utf-8'))
for i in range(len(expected_output)):
if echo:
index, match, buff = self.telnet.expect(expected_output, timeout=self.timeout)
index, match, buff = self.telnet.expect(self.prompts, timeout=self.timeout)
index, match, buff = self.telnet.expect([bytes(command, encoding='utf-8')],
    timeout=self.timeout)
buff = command + '\n'
buff = buff.decode('utf-8', 'replace')
buff = buff.decode('utf-8', 'replace')
buff = buff.decode('utf-8', 'replace')
if self.db.result:
if self.db.result:
if self.db.result:
self.db.result['debugger_output'] += buff
self.db.campaign['debugger_output'] += buff
self.db.result['debugger_output'] += buff
self.db.campaign['debugger_output'] += buff
self.db.result['debugger_output'] += buff
self.db.campaign['debugger_output'] += buff
if self.options.debug:
return_buffer += buff
return_buffer += buff
print(colored(buff, 'yellow'))
if echo and index < 0:
if self.options.debug:
if self.options.debug:
print(colored(buff, 'yellow'), end='')
if index < 0:
print(colored(buff, 'yellow'))
if self.db.result:
db.update('result')
db.update('campaign')
if index < 0:
for message in self.error_messages:
if message in return_buffer:
if log_event:
db.log_event_success(event)
return return_buffer
