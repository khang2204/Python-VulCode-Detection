def email_confirmation_redirect(request):...
response = HttpResponse('', status=302)
response['Location'] = '{}{}?{}'.format(settings.APP_DEEPLINK_DOMAIN,
    EMAIL_CONFIRMATION_PATH, request.GET.urlencode())
return response
