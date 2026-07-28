def launch_script(self, filename, *argv, **kwargs):...
if self.closed:
if self._adapter is not None:
assert self._session is None
argv = [filename] + list(argv)
if kwargs.pop('nodebug', False):
argv.insert(0, '--nodebug')
self._launch(argv, **kwargs)
return self._adapter, self._session
