def detectValidExtension(self, future):...
if not self.stopThreads:
html = future.result()[0].text
return None
ext = future.ext[0]
r = self.isASuccessfulUpload(html)
if r:
self.validExtensions.append(ext)
return r
if self.shouldLog:
self.logger.info('\x1b[1m\x1b[42mExtension %s seems valid for this form.\x1b[m'
    , ext)
if r != True:
self.logger.info(
    '\x1b[1;32mTrue regex matched the following information : %s\x1b[m', r)
