def detectCodeExec(self, url, regex):...
if self.shouldLog:
if self.logger.verbosity > 0:
r = self.session.get(url)
self.logger.debug('Requesting %s ...', url)
if self.shouldLog:
if r.status_code >= 400:
res = re.search(regex, r.text)
self.logger.warning('Code exec detection returned an http code of %s.', r.
    status_code)
self.httpRequests += 1
if res:
if self.logger.verbosity > 1:
return True
return False
printSimpleResponseObject(r)
if self.logger.verbosity > 2:
print('\x1b[36m' + r.text + '\x1b[m')
