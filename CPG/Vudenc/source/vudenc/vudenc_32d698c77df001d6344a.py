def post(self, request, *args, **kwargs):...
self.object = self.get_object()
form = self.get_form()
if form.is_valid():
return self.form_valid(form)
return self.form_invalid(form)
