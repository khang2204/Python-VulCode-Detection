@require_http_methods(['GET'])...
"""docstring"""
redirect_to = get_next_url_for_login_page(request)
if request.user.is_authenticated():
return redirect(redirect_to)
form_descriptions = _get_form_descriptions(request)
third_party_auth_hint = None
if '?' in redirect_to:
if is_request_in_themed_site() and not configuration_helpers.get_value(
next_args = urlparse.parse_qs(urlparse.urlparse(redirect_to).query)
if initial_mode == 'login':
ext_auth_response = _external_auth_intercept(request, initial_mode)
provider_id = next_args['tpa_hint'][0]
return old_login_view(request)
if initial_mode == 'register':
if ext_auth_response is not None:
tpa_hint_provider = third_party_auth.provider.Registry.get(provider_id=
    provider_id)
return old_register_view(request)
return ext_auth_response
account_activation_messages = [{'message': message.message, 'tags': message
    .tags} for message in messages.get_messages(request) if 
    'account-activation' in message.tags]
if tpa_hint_provider:
context = {'data': {'login_redirect_url': redirect_to, 'initial_mode':
    initial_mode, 'third_party_auth': _third_party_auth_context(request,
    redirect_to, third_party_auth_hint), 'third_party_auth_hint': 
    third_party_auth_hint or '', 'platform_name': configuration_helpers.
    get_value('PLATFORM_NAME', settings.PLATFORM_NAME), 'support_link':
    configuration_helpers.get_value('SUPPORT_SITE_LINK', settings.
    SUPPORT_SITE_LINK), 'password_reset_support_link': 
    configuration_helpers.get_value('PASSWORD_RESET_SUPPORT_LINK', settings
    .PASSWORD_RESET_SUPPORT_LINK) or settings.SUPPORT_SITE_LINK,
    'account_activation_messages': account_activation_messages,
    'login_form_desc': json.loads(form_descriptions['login']),
    'registration_form_desc': json.loads(form_descriptions['registration']),
    'password_reset_form_desc': json.loads(form_descriptions[
    'password_reset']), 'account_creation_allowed': configuration_helpers.
    get_value('ALLOW_PUBLIC_ACCOUNT_CREATION', settings.FEATURES.get(
    'ALLOW_PUBLIC_ACCOUNT_CREATION', True))}, 'login_redirect_url':
    redirect_to, 'responsive': True, 'allow_iframing': True,
    'disable_courseware_js': True, 'combined_login_and_register': True,
    'disable_footer': not configuration_helpers.get_value(
    'ENABLE_COMBINED_LOGIN_REGISTRATION_FOOTER', settings.FEATURES[
    'ENABLE_COMBINED_LOGIN_REGISTRATION_FOOTER'])}
if tpa_hint_provider.skip_hinted_login_dialog:
context = update_context_for_enterprise(request, context)
return redirect(pipeline.get_login_url(provider_id, pipeline.
    AUTH_ENTRY_LOGIN, redirect_url=redirect_to))
third_party_auth_hint = provider_id
response = render_to_response('student_account/login_and_register.html',
    context)
initial_mode = 'hinted_login'
response.delete_cookie(configuration_helpers.get_value(
    'ENTERPRISE_CUSTOMER_COOKIE_NAME', settings.
    ENTERPRISE_CUSTOMER_COOKIE_NAME), domain=configuration_helpers.
    get_value('BASE_COOKIE_DOMAIN', settings.BASE_COOKIE_DOMAIN))
return response
