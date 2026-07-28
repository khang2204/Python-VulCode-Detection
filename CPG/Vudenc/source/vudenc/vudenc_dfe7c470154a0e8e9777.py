def handler(self, resp, remote, *args, **kwargs):...
self.handled_resp = resp
self.handled_remote = remote
self.handled_args = args
self.handled_kwargs = kwargs
return 'TEST'
