def parse_body(self):...
"""docstring"""
expected = 'application/json', 'application/json; charset=utf-8'
if self.request.headers.get('Content-Type').lower() not in expected:
msg = "Expecting JSON body with content type 'application/json'"
body = json.loads(self.request.body)
self.abort(400, 'Not a valid json dict body')
return body
self.abort(400, msg)
if not isinstance(body, dict):
