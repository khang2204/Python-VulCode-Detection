def get_shib_info_from_request(request):...
info = {}
info['last_name'] = request.META.get('Shibboleth-sn', '')
info['first_name'] = request.META.get('Shibboleth-givenName', '')
info['email'] = request.META.get('Shibboleth-mail', '')
return info
