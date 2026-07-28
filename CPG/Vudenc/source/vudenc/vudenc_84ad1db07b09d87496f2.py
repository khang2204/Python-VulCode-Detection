def __init__(self, campaign_data, result_data, options, rsakey, aux=False):...
self.campaign_data = campaign_data
self.result_data = result_data
self.options = options
self.aux = aux
self.uboot_command = (self.options.dut_uboot if not self.aux else self.
    options.aux_uboot)
serial_port = options.dut_serial_port if not aux else options.aux_serial_port
baud_rate = options.dut_baud_rate if not aux else options.aux_baud_rate
self.serial = Serial(port=None, baudrate=baud_rate, timeout=options.timeout,
    rtscts=True)
if self.campaign_data['use_simics']:
self.serial._dsrdtr = True
self.serial.port = serial_port
self.serial.open()
self.serial.reset_input_buffer()
self.prompt = options.dut_prompt if not aux else options.aux_prompt
self.prompt += ' '
self.rsakey = rsakey
