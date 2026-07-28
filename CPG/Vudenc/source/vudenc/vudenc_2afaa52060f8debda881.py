@db.transact...
"""docstring"""
token = self.check_auth(request)
oms_root = db.get_root()['oms_root']
objs, unresolved_path = traverse_path(oms_root, request.path[1:])
if not objs and unresolved_path:
objs = [oms_root]
obj = objs[-1]
interaction = self.get_interaction(request, token)
request.interaction = interaction
if self.use_security_proxy:
obj = proxy_factory(obj, interaction)
view = self.find_view(obj, unresolved_path)
needs_rw_transaction = view.rw_transaction(request)
if interaction:
def get_renderer(view, method):...
view = proxy_factory(view, interaction)
return getattr(view, method, None)
from opennode.oms.endpoint.httprest.auth import IHttpRestAuthenticationUtility
for method in ('render_' + request.method, 'render'):
if token or not getUtility(IHttpRestAuthenticationUtility
renderer = get_renderer(view, method)
if renderer:
res = renderer(request)
if needs_rw_transaction:
return res
return db.RollbackValue(res)
