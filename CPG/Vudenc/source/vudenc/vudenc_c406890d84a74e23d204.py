def parse_body(self):...
"""docstring"""
if self._json_body is None:
if self.CONTENT_TYPE_BASE and self.request.content_type != self.CONTENT_TYPE_BASE:
return self._json_body.copy()
msg = "Expecting JSON body with content type '%s'" % self.CONTENT_TYPE_BASE
self._json_body = self.request.json
self.abort_with_error(400, text='Not a valid json dict body')
self.abort_with_error(400, text=msg)
if not isinstance(self._json_body, dict):
