def __str__(self):...
string = 'JTAG Debugger at ' + self.options.debugger_ip_address
string += ' port ' + str(self.port)
return string
