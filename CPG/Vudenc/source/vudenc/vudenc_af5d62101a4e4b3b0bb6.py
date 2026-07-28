def send_files(self, files, attempts=10):...
if self.options.debug:
print(colored('sending file(s)...', 'blue'), end='')
ssh = SSHClient()
ssh.set_missing_host_key_policy(AutoAddPolicy())
for attempt in range(attempts):
ssh.connect(self.ip_address, port=self.options.dut_scp_port if not self.aux
     else self.options.aux_scp_port, username='root', pkey=self.rsakey,
    allow_agent=False, look_for_keys=False)
if self.options.command != 'new':
dut_scp = SCPClient(ssh.get_transport())
db.log_event_exception(self.result_data['id'], 'DUT' if not self.aux else
    'AUX', 'SSH error')
print(colored(self.serial.port + ' ' + str(self.result_data['id']) +
    ': error sending file(s) (attempt ' + str(attempt + 1) + '/' + str(
    attempts) + '): ' + str(error), 'red'))
dut_scp.put(files)
if self.options.command != 'new':
dut_scp.close()
if attempt < attempts - 1:
db.log_event_exception(self.result_data['id'], 'DUT' if not self.aux else
    'AUX', 'SCP error')
print(colored(self.serial.port + ' ' + str(self.result_data['id']) +
    ': error sending file(s) (attempt ' + str(attempt + 1) + '/' + str(
    attempts) + '): ' + str(error), 'red'))
ssh.close()
sleep(30)
dut_scp.close()
if self.options.debug:
ssh.close()
print(colored('done', 'blue'))
if attempt < attempts - 1:
sleep(30)
