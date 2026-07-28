def _DoUnknown(self):...
self._WriteHeader('text/html', status_code=501)
self.wfile.write('<html><body>I do not know how to serve %s.</body></html>' %
    self.path)
