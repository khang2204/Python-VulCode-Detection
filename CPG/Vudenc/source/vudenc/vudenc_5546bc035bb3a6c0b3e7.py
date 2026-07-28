def get(self, request, **kwargs):...
if request.GET.get('keyword'):
ip = request.GET.get('keyword')
context = self.get_context_data()
return HttpResponseRedirect(ip)
return self.render_to_response(context)
