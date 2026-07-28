def close(self):...
self.telnet.write(bytes('shutdown\n', encoding='utf-8'))
super().close()
self.openocd.wait()
db.log_event('Information', 'Debugger', 'Closed openocd')
