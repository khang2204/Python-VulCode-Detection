def close(self):...
if self.telnet:
self.telnet.close()
self.dut.close()
db.log_event('Information', 'Debugger', 'Closed telnet')
if self.db.campaign['aux']:
self.aux.close()
