def __str__(self):...
string = 'Serial Port: ' + self.serial.port + '\n\tTimeout: ' + str(self.
    serial.timeout) + """ seconds
	Prompt: \"""" + self.prompt + '"'
string += '\n\tIP Address: ' + self.ip_address
string += '\n\tSCP Port: ' + str(self.options.dut_scp_port if not self.aux else
    self.options.aux_scp_port)
return string
