def process_view(self, request, view_func, view_args, view_kwargs):...
"""docstring"""
kbsite_name = view_kwargs.pop('kbsite_name', None)
if not kbsite_name:
kbsite_name = 'default'
request.kbsite = models.KegbotSite.objects.get(name=kbsite_name)
return None
