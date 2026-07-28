def render_recursive(self, request, depth):...
for method in ('render_' + request.method, 'render'):
if hasattr(self, method):
return self.filter_attributes(request, getattr(self, method)(request))
