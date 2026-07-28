def _WriteHeader(self, content_type='text/plain', status_code=200):...
self.send_response(status_code)
self.send_header('Content-Type', content_type)
self.end_headers()
