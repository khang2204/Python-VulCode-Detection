from urllib.parse import urlencode, quote_plus
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from experiences.factories import create_get_experience_interactor
from profiles.factories import create_get_profile_interactor
EMAIL_CONFIRMATION_PATH = '/people/me/email-confirmation'
LOGIN_PATH = '/people/me/login'
EXPERIENCE_PATH = '/e'
PROFILE_PATH = '/p'
EXPERIENCE_DEEPLINK_PATH = '/experiences'
PROFILE_DEEPLINK_PATH = '/profiles'
def email_confirmation_redirect(request):...
response = HttpResponse('', status=302)
response['Location'] = '{}{}?{}'.format(settings.APP_DEEPLINK_DOMAIN,
    EMAIL_CONFIRMATION_PATH, request.GET.urlencode())
return response
