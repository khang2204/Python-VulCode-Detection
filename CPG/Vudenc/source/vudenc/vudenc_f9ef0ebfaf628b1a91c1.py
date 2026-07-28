def login_redirect(request):...
response = HttpResponse('', status=302)
response['Location'] = '{}{}?{}'.format(settings.APP_DEEPLINK_DOMAIN,
    LOGIN_PATH, request.GET.urlencode())
return response
