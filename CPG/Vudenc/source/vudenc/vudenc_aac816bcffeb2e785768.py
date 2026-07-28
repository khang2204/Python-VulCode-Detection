def render_json(self, values, status=200):...
"""docstring"""
self._add_security_response_headers()
self.response.headers['Content-Type'] = 'application/json'
self.before_render_json(values, status)
self.response.out.write(json.dumps(values, cls=JsonEncoder))
self.response.set_status(status)
