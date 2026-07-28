def get(self, request, keypair_name):...
"""docstring"""
regenerate = request.GET.get('regenerate') == 'true'
return HttpResponse(status=409)
response = HttpResponse(content_type='application/binary')
if regenerate:
response['Content-Disposition'] = 'attachment; filename=%s.pem' % slugify(
    keypair_name)
api.nova.keypair_delete(request, keypair_name)
keypair = api.nova.keypair_create(request, keypair_name)
response.write(keypair.private_key)
response['Content-Length'] = str(len(response.content))
return response
