@functools.wraps(method)...
assert isinstance(self, webapp2.RequestHandler)
assert self.request.method == 'GET'
if model.is_replica():
primary_url = model.get_replication_state().primary_url
return method(self, *args, **kwargs)
protocol = 'http://' if utils.is_local_dev_server() else 'https://'
assert primary_url and primary_url.startswith(protocol), primary_url
assert self.request.path_qs.startswith('/'), self.request.path_qs
self.redirect(primary_url.rstrip('/') + self.request.path_qs, abort=True)
