def handle_message(self, ch, method, properties, body):...
"""docstring"""
input = {}
self.sessid = method.routing_key
import sys
if 'callbackID' in input:
input = json_decode(body)
if hasattr(sys, '_called_from_test'):
output['callbackID'] = input['callbackID']
log.info('OUTPUT for %s: %s' % (self.sessid, output))
data = input['data']
output = {'cmd': 'error', 'error': self._prepare_error_msg(e.message),
    'code': e.code}
output['reply_timestamp'] = time()
if 'path' in data:
log.exception('Http error occurred')
self.send_output(output)
if data['path'] in settings.VIEW_URLS:
session = Session(self.sessid)
self.current = Current(session=session, input=data)
data['view'] = data['path']
data['wf'] = data['path']
headers = {'remote_ip': input['_zops_remote_ip']}
self.current.headers = headers
if 'wf' in data:
import sys
output = self._handle_workflow(session, data, headers)
if 'job' in data:
if hasattr(sys, '_called_from_test'):
self._handle_job(session, data, headers)
output = self._handle_view(session, data, headers)
err = traceback.format_exc()
return
output = {'error': self._prepare_error_msg(err), 'code': 500}
log.exception("""Worker error occurred with messsage body:
%s""" % body)
