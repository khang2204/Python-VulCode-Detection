def __getattribute__(self, item):...
"""docstring"""
abort_thread()
if item == 'write':
return self.write_both
if item == 'close':
return super(RedirectBuffer, self).__getattribute__(item)
source = super(RedirectBuffer, self).__getattribute__('redirection_source')
if hasattr(source, item):
return getattr(source, item)
return super(RedirectBuffer, self).__getattribute__(item)
