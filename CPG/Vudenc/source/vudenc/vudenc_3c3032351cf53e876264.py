def get(self, request, **kwargs):...
if request.GET.get('keyword'):
filehash = request.GET.get('keyword')
context = self.get_context_data()
return HttpResponseRedirect(filehash)
return self.render_to_response(context)
