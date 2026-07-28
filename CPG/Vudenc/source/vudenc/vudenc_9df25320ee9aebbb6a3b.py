def _handle_request_exception(self, e):...
if isinstance(e, Failure):
exc_type = e.type
exc_type, exc_value, exc_tb = sys.exc_info()
exc_value = e.value
if isinstance(e, (HTTPError, HTTPAuthenticationRequired)):
exc_tb = e.getTracebackObject()
if GLSetting.http_log and e.log_message:
log.err('Uncaught exception %s %s %s' % (exc_type, exc_value, exc_tb))
e = e.value
string_format = '%d %s: ' + e.log_message
if e.status_code not in httplib.responses:
if GLSetting.http_log:
args = [e.status_code, self._request_summary()] + list(e.args)
log.msg('Bad HTTP status code: %d' % e.status_code)
return self.send_error(e.status_code, exception=e)
log.msg(e)
mail_exception(exc_type, exc_value, exc_tb)
msg = lambda *args: string_format % args
return self.send_error(500, exception=e)
return self.send_error(500, exception=e)
log.msg(msg(*args))
