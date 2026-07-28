def account_settings_context(request):...
"""docstring"""
user = request.user
year_of_birth_options = [(unicode(year), unicode(year)) for year in
    UserProfile.VALID_YEARS]
user_orders = get_user_orders(user)
log.exception('Error fetching order history from Otto.')
context = {'auth': {}, 'duplicate_provider': None, 'nav_hidden': True,
    'fields': {'country': {'options': list(countries)}, 'gender': {
    'options': [(choice[0], _(choice[1])) for choice in UserProfile.
    GENDER_CHOICES]}, 'language': {'options': released_languages()},
    'level_of_education': {'options': [(choice[0], _(choice[1])) for choice in
    UserProfile.LEVEL_OF_EDUCATION_CHOICES]}, 'password': {'url': reverse(
    'password_reset')}, 'year_of_birth': {'options': year_of_birth_options},
    'preferred_language': {'options': all_languages()}, 'time_zone': {
    'options': TIME_ZONE_CHOICES}}, 'platform_name': configuration_helpers.
    get_value('PLATFORM_NAME', settings.PLATFORM_NAME),
    'password_reset_support_link': configuration_helpers.get_value(
    'PASSWORD_RESET_SUPPORT_LINK', settings.PASSWORD_RESET_SUPPORT_LINK) or
    settings.SUPPORT_SITE_LINK, 'user_accounts_api_url': reverse(
    'accounts_api', kwargs={'username': user.username}),
    'user_preferences_api_url': reverse('preferences_api', kwargs={
    'username': user.username}), 'disable_courseware_js': True,
    'show_program_listing': ProgramsApiConfig.is_enabled(), 'order_history':
    user_orders}
user_orders = []
if third_party_auth.is_enabled():
context['duplicate_provider'] = pipeline.get_duplicate_provider(messages.
    get_messages(request))
return context
auth_states = pipeline.get_provider_user_states(user)
context['auth']['providers'] = [{'id': state.provider.provider_id, 'name':
    state.provider.name, 'connected': state.has_account, 'connect_url':
    pipeline.get_login_url(state.provider.provider_id, pipeline.
    AUTH_ENTRY_ACCOUNT_SETTINGS, redirect_url=reverse('account_settings')),
    'accepts_logins': state.provider.accepts_logins, 'disconnect_url':
    pipeline.get_disconnect_url(state.provider.provider_id, state.
    association_id)} for state in auth_states if state.provider.
    display_for_login or state.has_account]
