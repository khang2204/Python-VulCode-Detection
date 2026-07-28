def close(self):...
if self.telnet:
self.telnet.write(bytes('quit\r', encoding='utf-8'))
super().close()
