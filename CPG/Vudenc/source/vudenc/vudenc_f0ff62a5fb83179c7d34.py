def make_xsrf_handling_app(self, xsrf_token_enforce_on=None,...
"""docstring"""
calls = []
def record(request_handler, method):...
is_valid = request_handler.xsrf_token_data == {'some': 'data'}
calls.append((method, is_valid))
@api.public...
self.response.write(self.generate_xsrf_token({'some': 'data'}))
@api.public...
record(self, 'POST')
@api.public...
record(self, 'PUT')
@api.public...
record(self, 'DELETE')
if xsrf_token_enforce_on is not None:
Handler.xsrf_token_enforce_on = xsrf_token_enforce_on
if xsrf_token_header is not None:
Handler.xsrf_token_header = xsrf_token_header
if xsrf_token_request_param is not None:
Handler.xsrf_token_request_param = xsrf_token_request_param
app = self.make_test_app('/request', Handler)
return app, calls
