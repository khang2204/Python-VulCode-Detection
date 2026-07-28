def get(self, request, *args, **kwargs):...
if not request.user.is_authenticated:
return invalid_permission_redirect(request)
self.request = request
self.filter_data = kwargs.pop('filter_data', {})
return super().get(self, request, *args, **kwargs)
