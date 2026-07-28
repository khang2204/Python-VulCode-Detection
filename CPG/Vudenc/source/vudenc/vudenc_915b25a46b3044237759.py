def _render_access_form(self):...
self.object = self.report
self.template_name = self.access_template_name
context = self.get_context_data(form=self._get_access_form())
return self.render_to_response(context)
