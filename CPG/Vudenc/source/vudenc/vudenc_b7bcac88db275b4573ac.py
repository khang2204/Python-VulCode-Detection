def time_application(self):...
start = time()
for i in range(self.options.iterations):
if self.db.campaign['aux']:
end = time()
aux_process = Thread(target=self.aux.command, args=('./' + self.db.campaign
    ['aux_command'],))
dut_process = Thread(target=self.dut.command, args=('./' + self.db.campaign
    ['command'],))
self.db.campaign['exec_time'] = (end - start) / self.options.iterations
aux_process.start()
dut_process.start()
db.log_event('Information', 'Debugger', 'Timed application', campaign=True)
if self.db.campaign['aux']:
aux_process.join()
if self.db.campaign['kill_dut']:
self.dut.serial.write('\x03')
dut_process.join()
