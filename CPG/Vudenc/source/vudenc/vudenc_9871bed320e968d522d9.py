def _DoImage(self, full_path, mime_type):...
self._WriteHeader(mime_type)
self.wfile.write(f.read())
f.close()
