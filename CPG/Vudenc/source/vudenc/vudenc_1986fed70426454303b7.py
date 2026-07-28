def get(self, request, **kwargs):...
if request.GET.get('keyword'):
domain = request.GET.get('keyword')
context = self.get_context_data()
return HttpResponseRedirect(domain)
return self.render_to_response(context)
