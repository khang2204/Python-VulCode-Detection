def handle_post(self):...
self.log('')
self.log('POST ' + self.req)
if self.headers['expect'].lower() == '100-continue':
self.parser = MultipartParser(self.log, self.sr, self.headers)
self.s.send(b'HTTP/1.1 100 Continue\r\n\r\n')
self.parser.parse()
act = self.parser.require('act', 64)
if act == u'bput':
self.handle_plain_upload()
if act == u'login':
return
self.handle_login()
return
