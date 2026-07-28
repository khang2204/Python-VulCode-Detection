def setup(self, initUrl):...
self.formUrl = initUrl
url = urlparse(self.formUrl)
self.schema = url.scheme
self.host = url.netloc
self.httpRequests = 0
initGet = self.session.get(self.formUrl, headers={'Accept-Encoding': None})
self.logger.critical('%s : Host unreachable (%s)', getHost(initUrl), e)
detectedForms = detectForms(initGet.text)
self.httpRequests += 1
exit()
if len(detectedForms) == 0:
if self.logger.verbosity > 1:
self.logger.critical('No HTML form found here')
if len(detectedForms) > 1:
printSimpleResponseObject(initGet)
if self.logger.verbosity > 2:
exit()
self.logger.critical(
    '%s forms found containing file upload inputs, no way to choose which one to test.'
    , len(detectedForms))
if len(detectedForms[0][1]) > 1:
print('\x1b[36m' + initGet.text + '\x1b[m')
if initGet.status_code < 200 or initGet.status_code > 300:
exit()
self.logger.critical(
    '%s file inputs found inside the same form, no way to choose which one to test.'
    , len(detectedForms[0]))
self.inputName = detectedForms[0][1][0]['name']
self.logger.critical('Server responded with following status : %s - %s',
    initGet.status_code, initGet.reason)
exit()
self.logger.debug('Found the following file upload input : %s', self.inputName)
exit()
formDestination = detectedForms[0][0]
self.action = formDestination['action']
self.action = ''
self.uploadUrl = urljoin(self.formUrl, self.action)
self.logger.debug('Using following URL for file upload : %s', self.uploadUrl)
if not self.uploadsFolder and not self.trueRegex:
self.logger.warning(
    'No uploads folder nor true regex defined, code execution detection will not be possible.'
    )
if not self.uploadsFolder and self.trueRegex:
print(
    'No uploads path provided, code detection can still be done using true regex capturing group.'
    )
cont = input(
    'Do you want to use the True Regex for code execution detection ? [Y/n] ')
if cont.lower().startswith('y') or cont == '':
preffixPattern = input('Preffix capturing group of the true regex with : ')
self.logger.warning(
    'Code execution detection will not be possible as there is no path nor regex pattern configured.'
    )
suffixPattern = input('Suffix capturing group of the true regex with : ')
self.codeExecUrlPattern = preffixPattern + '$captGroup$' + suffixPattern
