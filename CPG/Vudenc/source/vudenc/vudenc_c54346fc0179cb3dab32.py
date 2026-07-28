def view(request, *args, **kwargs):...
self = cls(**initkwargs)
if hasattr(self, 'get') and not hasattr(self, 'head'):
self.head = self.get
self.request = request
self.args = args
self.kwargs = kwargs
self.setup(request, *args, **kwargs)
return self.dispatch(request, *args, **kwargs)
