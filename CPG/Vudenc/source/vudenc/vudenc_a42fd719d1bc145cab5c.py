def reset_bdi(self):...
event = db.log_event('Warning', 'Debugger', 'Reset BDI', success=False)
self.telnet.write(bytes('boot\r\n', encoding='utf-8'))
self.telnet.close()
if self.db.result:
self.db.result['debugger_output'] += 'boot\n'
self.db.campaign['debugger_output'] += 'boot\n'
sleep(1)
self.connect_telnet()
sleep(1)
self.command(None, error_message='', log_event=False)
db.log_event_success(event)
