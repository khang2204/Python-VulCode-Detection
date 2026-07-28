def get(self, request, *args, **kwargs):...
form = self.get_form()
if form.is_valid():
return self.form_valid(form)
return self.render_to_response(self.get_context_data())
