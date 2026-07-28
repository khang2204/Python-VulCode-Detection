def profile_redirect(request, username):...
dynamic_link = settings.DYNAMIC_LINK
if len(dynamic_link) > 0:
real_link = '{}{}/{}'.format(settings.PUBLIC_DOMAIN, PROFILE_PATH, username)
link = '{}{}/{}'.format(settings.APP_DEEPLINK_DOMAIN, PROFILE_DEEPLINK_PATH,
    username)
link = dynamic_link.format(real_link)
response = HttpResponse('', status=302)
get_profile_interactor = create_get_profile_interactor()
response['Location'] = link
profile = get_profile_interactor.set_params(username=username,
    logged_person_id='-1').execute()
return response
preview_content = {'st': '@{}'.format(profile.username), 'sd': profile.bio,
    'si': profile.picture.small_url}
preview_encoded = urlencode(preview_content, quote_via=quote_plus)
link = '{}&{}'.format(link, preview_encoded)
