def new_connection(self, cluster_api, provider):...
session = super(NsxClientTestCase.MockHTTPProvider, self).new_connection(
    cluster_api, provider)
mock_adapter = mock.Mock()
session_send = session.send
def _adapter_send(request, **kwargs):...
mock_response = mock.Mock()
mock_response.history = None
mock_response.headers = {'location': ''}
mock_response.raw._original_response = {}
cluster_api.record_call(request, **kwargs)
return mock_response
