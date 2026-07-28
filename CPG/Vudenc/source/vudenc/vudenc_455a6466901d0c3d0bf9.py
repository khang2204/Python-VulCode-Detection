def send_dut_files(self, aux=False):...
location = 'campaign-data/' + str(self.campaign_data['id'])
if aux:
location += '/aux-files/'
location += '/dut-files/'
files = []
for item in os.listdir(location):
files.append(location + item)
if aux:
self.debugger.aux.send_files(files)
self.debugger.dut.send_files(files)
