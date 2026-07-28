def supervise(self, iteration_counter, packet_capture):...
interrupted = False
while not interrupted:
iteration = iteration_counter.value
if iteration:
iteration_counter.value -= 1
self.create_result()
if packet_capture:
data_dir = 'campaign-data/' + str(self.campaign_data['id']
    ) + '/results/' + str(self.result_data['id'])
if self.campaign_data['use_aux']:
os.makedirs(data_dir)
self.debugger.aux.write('./' + self.campaign_data['aux_command'] + '\n')
self.debugger.dut.write('./' + self.campaign_data['command'] + '\n')
capture_file = open(data_dir + '/capture.pcap', 'w')
self.result_data['outcome'], self.result_data['outcome_category'
    ] = self.__monitor_execution()
if self.campaign_data['use_simics']:
self.log_result()
capture_process = Popen(['ssh', 'p2020', 'tshark -F pcap -i eth1 -w -'],
    stderr=PIPE, stdout=capture_file)
self.debugger.continue_dut()
self.debugger.dut.serial.write('\x03')
if packet_capture:
buff = ''
self.debugger.dut.read_until()
os.system("ssh p2020 'killall tshark'")
while True:
if self.campaign_data['use_aux']:
capture_process.wait()
buff += capture_process.stderr.read(1)
self.debugger.aux.serial.write('\x03')
self.result_data.update({'outcome_category': 'Incomplete', 'outcome':
    'Interrupted'})
capture_file.close()
if buff[-len("Capturing on 'eth1'"):] == "Capturing on 'eth1'":
self.debugger.aux.read_until()
interrupted = True
