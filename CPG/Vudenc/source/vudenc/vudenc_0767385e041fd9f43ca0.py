def send_default(self, cmdname, *args, **kwargs):...
"""docstring"""
if not cmdname == 'options':
self.client.lineSend(self.csessid, [cmdname, args, kwargs])
