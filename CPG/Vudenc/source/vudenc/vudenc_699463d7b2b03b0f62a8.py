def forbid_ui_on_replica(method):...
"""docstring"""
@functools.wraps(method)...
assert isinstance(self, webapp2.RequestHandler)
if model.is_replica():
primary_url = model.get_replication_state().primary_url
return method(self, *args, **kwargs)
self.abort(405, detail='Not allowed on a replica, see primary at %s' %
    primary_url)
