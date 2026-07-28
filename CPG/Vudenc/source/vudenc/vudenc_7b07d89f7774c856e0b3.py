def __enter__(self):...
"""docstring"""
if self._bin_found is None:
if not os.path.exists(self.binary):
if not self._bin_found:
self._bin_found = True
self.go_get()
self._bin_found = False
return self.gometalinter()
self._install_linters()
