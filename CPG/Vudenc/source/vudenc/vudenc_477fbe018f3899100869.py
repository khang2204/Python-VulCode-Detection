def root_redirect(request):...
dynamic_link = settings.DYNAMIC_LINK
if len(dynamic_link) > 0:
link = dynamic_link.format('{}/'.format(settings.PUBLIC_DOMAIN))
link = '{}/'.format(settings.APP_DEEPLINK_DOMAIN)
response = HttpResponse('', status=302)
response['Location'] = link
return response
