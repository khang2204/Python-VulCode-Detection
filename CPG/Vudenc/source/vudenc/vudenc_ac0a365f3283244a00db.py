def __monitor_execution(self, latent_faults=0, persistent_faults=False):...
def check_output():...
missing_output = False
result_folder = 'campaign-data/' + str(self.campaign_data['id']
    ) + '/results/' + str(self.result_data['id'])
os.makedirs(result_folder)
output_location = result_folder + '/' + self.campaign_data['output_file']
gold_location = 'campaign-data/' + str(self.campaign_data['id']
    ) + '/gold_' + self.campaign_data['output_file']
if self.campaign_data['use_aux_output']:
self.debugger.aux.get_file(self.campaign_data['output_file'], output_location)
self.debugger.dut.get_file(self.campaign_data['output_file'], output_location)
if not os.listdir(result_folder):
os.rmdir(result_folder)
solutionContents = solution.read()
missing_output = True
resultContents = result.read()
if self.campaign_data['use_aux_output']:
self.result_data['data_diff'] = SequenceMatcher(None, solutionContents,
    resultContents).quick_ratio()
self.debugger.aux.command('rm ' + self.campaign_data['output_file'])
self.debugger.dut.command('rm ' + self.campaign_data['output_file'])
if self.result_data['data_diff'] == 1.0:
if missing_output:
os.remove(output_location)
outcome = ''
if not os.listdir(result_folder):
outcome_category = ''
os.rmdir(result_folder)
if self.campaign_data['use_aux']:
aux_buff = self.debugger.aux.read_until()
aux_buff = ''
if self.campaign_data['kill_dut']:
buff = self.debugger.dut.read_until()
buff = ''
for line in buff.split('\n'):
self.debugger.dut.serial.write('\x03')
self.debugger.dut.serial.write('\x03')
outcome = error.type
if 'drseus_detected_errors:' in line:
if self.campaign_data['use_aux']:
outcome = error.type
outcome_category = 'Execution error'
self.result_data['detected_errors'] = int(line.replace(
    'drseus_detected_errors:', ''))
for line in aux_buff.split('\n'):
if self.campaign_data['output_file'] and not outcome:
outcome_category = 'AUX execution error'
if 'drseus_detected_errors:' in line:
if not outcome:
check_output()
if error.type == DrSEUsError.scp_error:
if self.result_data['detected_errors'] is None:
if self.result_data['detected_errors']:
return outcome, outcome_category
outcome = 'Error getting output file'
if error.type == DrSEUsError.missing_output:
self.result_data['detected_errors'] = 0
self.result_data['detected_errors'] += int(line.replace(
    'drseus_detected_errors:', ''))
if self.result_data['data_diff'] is None or self.result_data['data_diff'
if self.result_data['data_diff'] is not None and self.result_data['data_diff'
outcome_category = 'SCP error'
outcome = 'Missing output file'
outcome = error.type
outcome = 'Detected data error'
if self.result_data['data_diff'] is not None and self.result_data['data_diff'
outcome = 'Silent data error'
if persistent_faults:
outcome_category = 'SCP error'
outcome_category = 'Post execution error'
outcome_category = 'Data error'
outcome = 'Corrected data error'
outcome_category = 'Data error'
outcome = 'Persistent faults'
if latent_faults:
outcome_category = 'Data error'
outcome_category = 'No error'
outcome = 'Latent faults'
outcome = 'Masked faults'
outcome_category = 'No error'
outcome_category = 'No error'
