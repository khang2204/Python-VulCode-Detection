def setup_campaign(self):...
files = []
files.append(self.options.directory + '/' + self.options.application)
if self.options.files:
for file_ in self.options.files:
os.makedirs('campaign-data/' + str(self.campaign_data['id']) + '/dut-files')
files.append(self.options.directory + '/' + file_)
for item in files:
copy(item, 'campaign-data/' + str(self.campaign_data['id']) + '/dut-files/')
if self.campaign_data['use_aux']:
aux_files = []
self.debugger.dut.send_files(files)
aux_files.append(self.options.directory + '/' + self.options.aux_application)
if self.campaign_data['use_aux']:
if self.options.aux_files:
aux_process.join()
self.debugger.dut.command()
for file_ in self.options.aux_files:
os.makedirs('campaign-data/' + str(self.campaign_data['id']) + '/aux-files')
aux_process = Thread(target=self.debugger.aux.command)
if self.campaign_data['use_aux']:
aux_files.append(self.options.directory + '/' + file_)
for item in aux_files:
aux_process.start()
aux_process.join()
self.debugger.time_application()
copy(item, 'campaign-data/' + str(self.campaign_data['id']) + '/aux-files/')
aux_process = Thread(target=self.debugger.aux.send_files, args=(aux_files,))
if self.campaign_data['output_file']:
aux_process.start()
if self.campaign_data['use_aux_output']:
if self.campaign_data['use_simics']:
self.debugger.aux.get_file(self.campaign_data['output_file'], 
    'campaign-data/' + str(self.campaign_data['id']) + '/gold_' + self.
    campaign_data['output_file'])
self.debugger.dut.get_file(self.campaign_data['output_file'], 
    'campaign-data/' + str(self.campaign_data['id']) + '/gold_' + self.
    campaign_data['output_file'])
self.debugger.close()
db.update_dict('campaign', self.campaign_data)
self.close()
