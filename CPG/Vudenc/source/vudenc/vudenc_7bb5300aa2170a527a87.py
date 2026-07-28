def read_until(self, string=None, continuous=False, boot=False):...
if string is None:
string = self.prompt
buff = ''
event_buff = ''
event_buff_logged = ''
errors = 0
while True:
char = self.serial.read().decode('utf-8', 'replace')
if not char:
if self.options.command != 'new':
if self.options.command == 'new':
event_buff = buff.replace(event_buff_logged, '')
if not continuous:
self.campaign_data['dut_output' if not self.aux else 'aux_output'] += char
self.result_data['dut_output' if not self.aux else 'aux_output'] += char
db.log_event(self.result_data['id'], 'DUT' if not self.aux else 'AUX',
    'Read timeout', event_buff)
if self.serial.timeout != self.options.timeout:
if self.options.debug:
event_buff_logged += event_buff
self.serial.timeout = self.options.timeout
if self.options.debug:
print(colored(char, 'green' if not self.aux else 'cyan'), end='')
buff += char
print()
if self.options.command == 'new':
sys.stdout.flush()
if not continuous and buff[-len(string):] == string:
db.update_dict('campaign', self.campaign_data)
db.update_dict('result', self.result_data)
if buff[-len('autoboot: '):] == 'autoboot: ' and self.uboot_command:
if errors and not boot:
self.write('\n')
if buff[-len('login: '):] == 'login: ':
for message, category in self.error_messages:
return buff
self.write(self.uboot_command + '\n')
self.write(self.options.username + '\n')
if buff[-len('Password: '):] == 'Password: ':
if message in buff:
for message, category in self.error_messages:
self.write(self.options.password + '\n')
if buff[-len("can't get kernel image"):] == "can't get kernel image":
if buff[-len(message):] == message:
if not continuous and errors > 10:
self.write('reset\n')
if not continuous and not boot:
if not boot and buff and buff[-1] == '\n':
errors += 1
self.serial.timeout = 30
if self.options.command != 'new' and not boot:
if self.options.command == 'new':
errors += 1
event_buff = buff.replace(event_buff_logged, '')
db.update_dict('campaign', self.campaign_data)
db.update_dict('result', self.result_data)
db.log_event(self.result_data['id'], 'DUT' if not self.aux else 'AUX',
    category, event_buff)
event_buff_logged += event_buff
