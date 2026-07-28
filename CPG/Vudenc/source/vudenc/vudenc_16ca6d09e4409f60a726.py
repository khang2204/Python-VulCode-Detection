def abort_with_error(self, http_code, **kwargs):...
"""docstring"""
self.abort(http_code, json=kwargs, headers={'Content-Type': self.
    CONTENT_TYPE_FULL})
