def __init__(self, campaign_data, options):...
self.campaign_data = campaign_data
self.options = options
self.result_data = {'campaign_id': self.campaign_data['id'], 'aux_output':
    '', 'data_diff': None, 'debugger_output': '', 'detected_errors': None,
    'dut_output': ''}
if os.path.exists('campaign-data/' + str(campaign_data['id']) + '/private.key'
self.rsakey = RSAKey.from_private_key_file('campaign-data/' + str(
    campaign_data['id']) + '/private.key')
self.rsakey = RSAKey.generate(1024)
if self.campaign_data['use_simics']:
self.rsakey.write_private_key_file('campaign-data/' + str(campaign_data[
    'id']) + '/private.key')
self.debugger = simics(campaign_data, self.result_data, options, self.rsakey)
if campaign_data['architecture'] == 'p2020':
if not self.campaign_data['use_simics']:
self.debugger = bdi_p2020(campaign_data, self.result_data, options, self.rsakey
    )
if campaign_data['architecture'] == 'a9':
if self.campaign_data['use_aux']:
self.debugger = openocd(campaign_data, self.result_data, options, self.rsakey)
self.debugger.aux.serial.write('\x03')
if options.command == 'new':
self.debugger.aux.do_login()
self.debugger.reset_dut()
if options.command != 'new':
self.send_dut_files(aux=True)
