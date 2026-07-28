def experience_redirect(request, experience_share_id):...
dynamic_link = settings.DYNAMIC_LINK
if len(dynamic_link) > 0:
real_link = '{}{}/{}'.format(settings.PUBLIC_DOMAIN, EXPERIENCE_PATH,
    experience_share_id)
link = '{}{}/{}'.format(settings.APP_DEEPLINK_DOMAIN,
    EXPERIENCE_DEEPLINK_PATH, experience_share_id)
link = dynamic_link.format(real_link)
response = HttpResponse('', status=302)
get_experience_interactor = create_get_experience_interactor()
response['Location'] = link
experience = get_experience_interactor.set_params(experience_share_id=
    experience_share_id, logged_person_id='-1').execute()
return response
desc = experience.description[:77] + '...' if len(experience.description
    ) > 77 else experience.description
preview_content = {'st': experience.title, 'sd': desc, 'si': experience.
    picture.small_url}
preview_encoded = urlencode(preview_content, quote_via=quote_plus)
link = '{}&{}'.format(link, preview_encoded)
