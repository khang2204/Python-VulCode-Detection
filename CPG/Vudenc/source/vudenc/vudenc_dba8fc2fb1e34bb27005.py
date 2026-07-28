def uploadFile(self, suffix, mime, payload):...
fd.write(payload)
fd.flush()
fd.seek(0)
filename = os.path.basename(fd.name)
if self.shouldLog:
self.logger.debug('Sending file %s with mime type : %s', filename, mime)
fu = self.session.post(self.uploadUrl, files={self.inputName: (filename, fd,
    mime)}, data=self.postData)
self.httpRequests += 1
if self.shouldLog:
if self.logger.verbosity > 1:
return fu, filename
printSimpleResponseObject(fu)
if self.logger.verbosity > 2:
print('\x1b[36m' + fu.text + '\x1b[m')
