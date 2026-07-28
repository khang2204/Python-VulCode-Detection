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
if not os.listdir(result_folder):
os.rmdir(result_folder)
