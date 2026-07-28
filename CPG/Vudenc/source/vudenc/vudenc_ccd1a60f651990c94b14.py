def send_response(self, response, http_code=200, headers=None):...
"""docstring"""
self.response.set_status(http_code)
self.response.headers.update(headers or {})
self.response.headers['Content-Type'] = self.CONTENT_TYPE_FULL
self.response.write(json.dumps(response))
