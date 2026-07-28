def process_view(self, request, view_func, view_args, view_kwargs):...
if not hasattr(request, 'kbsite'):
return None
kbsite = request.kbsite
if kbsite.is_active:
return None
if self._path_allowed(request.path):
return None
if request.user.is_staff or request.user.is_superuser:
return None
return HttpResponse('Site temporarily unavailable', status=503)
