def __init__(self, session_response=None):...
super(NsxClientTestCase.MockHTTPProvider, self).__init__()
if isinstance(session_response, list):
self._session_responses = session_response
if session_response:
self._session_responses = [session_response]
self._session_responses = None
