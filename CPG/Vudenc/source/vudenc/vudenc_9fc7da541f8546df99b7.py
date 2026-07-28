def _rpc(self, method, *args):...
"""docstring"""
apiid = next(self._counter)
data = {'id': apiid, 'method': method, 'params': args}
request = json.dumps(data)
self._client.write(request.encode('utf8') + b'\n')
self._client.flush()
response = self._client.readline()
if not response:
result = json.loads(str(response, encoding='utf8'))
if result['error']:
if result['id'] != apiid:
if result.get('callback') is not None:
if self._event_client is None:
return result['result']
self._event_client = self._start_event_client()
return callback_handler.CallbackHandler(callback_id=result['callback'],
    event_client=self._event_client, ret_value=result['result'],
    method_name=method)
