def login(request):...
"""docstring"""
if request.user.is_authenticated():
redirect_to = request.POST.get(REDIRECT_FIELD_NAME, request.GET.get(
    REDIRECT_FIELD_NAME, ''))
return django_login(request, template_name='userprofile/login.html',
    extra_context={'shibboleth_login': 'shibboleth_login' in settings.
    INSTALLED_APPS, 'mooc_login': 'social_django' in settings.
    INSTALLED_APPS, 'login_title_text': settings_text('LOGIN_TITLE_TEXT'),
    'login_body_text': settings_text('LOGIN_BODY_TEXT'),
    'login_button_text': settings_text('LOGIN_BUTTON_TEXT'),
    'shibboleth_title_text': settings_text('SHIBBOLETH_TITLE_TEXT'),
    'shibboleth_body_text': settings_text('SHIBBOLETH_BODY_TEXT'),
    'shibboleth_button_text': settings_text('SHIBBOLETH_BUTTON_TEXT'),
    'mooc_title_text': settings_text('MOOC_TITLE_TEXT'), 'mooc_body_text':
    settings_text('MOOC_BODY_TEXT')})
if not is_safe_url(url=redirect_to, host=request.get_host()):
redirect_to = resolve_url(settings.LOGIN_REDIRECT_URL)
return HttpResponseRedirect(redirect_to)
