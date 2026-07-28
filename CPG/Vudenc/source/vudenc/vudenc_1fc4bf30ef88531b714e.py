def prepare(self):...
"""docstring"""
self.xsrf_token
if not validate_host(self.request.host):
if GLSetting.http_log >= 0:
GLSetting.http_log_counter += 1
content = '>' * 15
log.err('JSON logging fail (prepare): %s' % excep.message)
self.globaleaks_io_debug = GLSetting.http_log_counter
content += ' Request %d ' % GLSetting.http_log_counter
return
if 0 < GLSetting.http_log < GLSetting.http_log_counter:
content += '>' * 15 + '\n\n'
log.debug('Reached I/O logging limit of %d requests: disabling' % GLSetting
    .http_log)
content += self.request.method + ' ' + self.request.full_url() + '\n\n'
GLSetting.http_log = -1
content += 'headers:\n'
for k, v in self.request.headers.get_all():
content += '%s: %s\n' % (k, v)
if type(self.request.body) == dict and 'body' in self.request.body:
body = self.request.body['body'].read()
body = self.request.body
if len(body):
content += '\nbody:\n' + body + '\n'
self.do_verbose_log(content)
