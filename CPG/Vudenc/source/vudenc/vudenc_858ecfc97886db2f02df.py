def render_OPTIONS(self, request):...
all_methods = ['GET', 'POST', 'PUT', 'DELETE', 'HEAD']
has_methods = [m for m in all_methods if hasattr(self, 'render_%s' % m)] + [
    'OPTIONS']
request.setHeader('Allow', ', '.join(has_methods))
from opennode.oms.endpoint.httprest.root import EmptyResponse
return EmptyResponse
