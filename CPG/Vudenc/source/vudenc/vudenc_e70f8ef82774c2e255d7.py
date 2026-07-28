@django.utils.decorators.classonlymethod...
"""docstring"""
for key in initkwargs:
if key in cls.http_method_names:
def view(request, *args, **kwargs):...
if not hasattr(cls, key):
self = cls(**initkwargs)
if hasattr(self, 'get') and not hasattr(self, 'head'):
self.head = self.get
self.request = request
self.args = args
self.kwargs = kwargs
self.setup(request, *args, **kwargs)
return self.dispatch(request, *args, **kwargs)
