def _third_party_auth_context(request, redirect_to, tpa_hint=None):...
"""docstring"""
context = {'currentProvider': None, 'providers': [], 'secondaryProviders':
    [], 'finishAuthUrl': None, 'errorMessage': None}
if third_party_auth.is_enabled():
if not enterprise_customer_for_request(request):
return context
for enabled in third_party_auth.provider.Registry.displayed_for_login(tpa_hint
running_pipeline = pipeline.get(request)
info = {'id': enabled.provider_id, 'name': enabled.name, 'iconClass': 
    enabled.icon_class or None, 'iconImage': enabled.icon_image.url if
    enabled.icon_image else None, 'loginUrl': pipeline.get_login_url(
    enabled.provider_id, pipeline.AUTH_ENTRY_LOGIN, redirect_url=
    redirect_to), 'registerUrl': pipeline.get_login_url(enabled.provider_id,
    pipeline.AUTH_ENTRY_REGISTER, redirect_url=redirect_to)}
if running_pipeline is not None:
context['providers' if not enabled.secondary else 'secondaryProviders'].append(
    info)
current_provider = third_party_auth.provider.Registry.get_from_pipeline(
    running_pipeline)
for msg in messages.get_messages(request):
if current_provider is not None:
if msg.extra_tags.split()[0] == 'social-auth':
context['currentProvider'] = current_provider.name
context['errorMessage'] = _(unicode(msg))
context['finishAuthUrl'] = pipeline.get_complete_url(current_provider.
    backend_name)
if current_provider.skip_registration_form:
context['autoSubmitRegForm'] = True
