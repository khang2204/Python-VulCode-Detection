def inject_and_monitor(self, iteration_counter):...
while True:
if iteration_counter is not None:
iteration = iteration_counter.value
self.create_result(self.options.injections)
if iteration:
if not self.campaign_data['use_simics']:
iteration_counter.value -= 1
self.close()
attempts = 10
if self.campaign_data['use_aux'] and not self.campaign_data['use_simics']:
for attempt in range(attempts):
self.debugger.aux.write('./' + self.campaign_data['aux_command'] + '\n')
latent_faults, persistent_faults = self.debugger.inject_faults()
self.result_data['outcome'] = error.type
self.result_data['outcome'], self.result_data['outcome_category'
    ] = self.__monitor_execution(latent_faults, persistent_faults)
self.debugger.reset_dut()
db.log_event_exception(self.result_data['id'], 'Debugger',
    'Error resetting DUT')
self.send_dut_files()
self.result_data.update({'outcome_category': error.type, 'outcome':
    'Error sending files to DUT'})
self.debugger.continue_dut()
if self.campaign_data['use_simics']:
if self.result_data['outcome'] == 'Latent faults' or not self.campaign_data[
print(colored(self.debugger.dut.serial.port + ' ' + str(self.result_data[
    'id']) + ': Error resetting DUT (attempt ' + str(attempt + 1) + '/' +
    str(attempts) + '): ' + str(error), 'red'))
self.log_result()
if self.campaign_data['use_simics']:
self.result_data['outcome_category'] = 'Simics error'
self.result_data['outcome_category'] = 'Debugger error'
if self.campaign_data['use_aux']:
if attempt < attempts - 1:
self.log_result()
self.debugger.close()
self.result_data.update({'outcome_category': 'Simics error', 'outcome':
    error.type})
rmtree('simics-workspace/injected-checkpoints/' + str(self.campaign_data[
    'id']) + '/' + str(self.result_data['id']))
if not self.campaign_data['use_simics']:
self.debugger.aux.write('./' + self.campaign_data['aux_command'] + '\n')
self.debugger.dut.write('./' + self.campaign_data['command'] + '\n')
sleep(30)
self.result_data.update({'outcome_category': 'Debugger error', 'outcome':
    'Error resetting dut'})
self.debugger.continue_dut()
next_outcome = self.__monitor_execution()[0]
self.log_result()
if self.campaign_data['use_aux']:
if next_outcome != 'Masked faults':
self.close()
aux_process = Thread(target=self.debugger.aux.read_until)
self.debugger.dut.read_until()
self.result_data.update({'outcome_category': 'Post execution error',
    'outcome': next_outcome})
return
aux_process.start()
if self.campaign_data['use_aux']:
aux_process.join()
