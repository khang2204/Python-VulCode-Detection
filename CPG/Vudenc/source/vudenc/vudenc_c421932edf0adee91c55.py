def not_applicable(request):...
self.assertEqual('/request', request.path)
calls.append('not_applicable')
return None
