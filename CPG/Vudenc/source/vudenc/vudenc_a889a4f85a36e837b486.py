def connect_telnet(self):...
self.telnet = Telnet(self.options.debugger_ip_address, self.port, timeout=
    self.timeout)
db.log_event('Information', 'Debugger', 'Connected to telnet', self.options
    .debugger_ip_address + ':' + str(self.port))
