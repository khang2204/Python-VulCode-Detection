def submitTestCase(self, suffix, mime, payload=None, codeExecRegex=None):...
fu = self.uploadFile(suffix, mime, payload)
uploadRes = self.isASuccessfulUpload(fu[0].text)
result = {'uploaded': False, 'codeExec': False}
if uploadRes:
result['uploaded'] = True
return result
if self.shouldLog:
self.logger.info("\x1b[1;32mUpload of '%s' with mime type %s successful\x1b[m",
    fu[1], mime)
if uploadRes != True:
if self.shouldLog:
if codeExecRegex and valid_regex(codeExecRegex) and (self.uploadsFolder or
self.logger.info(
    '\x1b[1;32m\tTrue regex matched the following information : %s\x1b[m',
    uploadRes)
url = None
secondUrl = None
if self.uploadsFolder:
url = self.schema + '://' + self.host + '/' + self.uploadsFolder + '/' + fu[1]
if self.codeExecUrlPattern:
filename = fu[1]
url = self.codeExecUrlPattern.replace('$captGroup$', uploadRes)
if url:
secondUrl = None
executedCode = self.detectCodeExec(url, codeExecRegex)
if secondUrl:
for b in getPoisoningBytes():
if executedCode:
executedCode = self.detectCodeExec(secondUrl, codeExecRegex)
if b in filename:
result['codeExec'] = True
if executedCode:
secondUrl = b.join(url.split(b)[:-1])
result['codeExec'] = True
