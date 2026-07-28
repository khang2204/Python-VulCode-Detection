def test_client_validate_result(self):...
def _verb_response_code(http_verb, status_code, error_code=None):...
content = None
if error_code:
content = jsonutils.dumps({'httpStatus': 'dummy', 'error_code': error_code,
    'module_name': 'dummy', 'error_message': 'bad'})
response = mocks.MockRequestsResponse(status_code, content)
client_api = self.new_mocked_client(client.RESTClient, mock_validate=False,
    session_response=response)
client_call = getattr(client_api, 'url_%s' % http_verb)
client_call('', None)
for verb in ['get', 'post', 'put', 'delete']:
for code in client.RESTClient._VERB_RESP_CODES.get(verb):
_verb_response_code(verb, code)
self.assertRaises(nsxlib_exc.ManagerError, _verb_response_code, verb,
    requests.codes.INTERNAL_SERVER_ERROR)
self.assertRaises(nsxlib_exc.ResourceNotFound, _verb_response_code, verb,
    requests.codes.NOT_FOUND)
self.assertRaises(nsxlib_exc.BackendResourceNotFound, _verb_response_code,
    verb, requests.codes.NOT_FOUND, 202)
