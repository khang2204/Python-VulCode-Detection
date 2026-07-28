def launch_module(self, module, *argv, **kwargs):...
if self.closed:
if self._adapter is not None:
assert self._session is None
argv = ['-m', module] + list(argv)
if kwargs.pop('nodebug', False):
argv.insert(0, '--nodebug')
self._launch(argv, **kwargs)
return self._adapter, self._session
