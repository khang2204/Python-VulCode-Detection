import json
from django.conf import settings
from django.test import TestCase, Client
from django.urls import reverse
from experiences.models import ORMExperience
from people.models import ORMPerson
from profiles.models import ORMProfile
def test_when_called_redirect_view_redirects_to_apps_url(self):...
RedirectConfirmEmailTestCase.ScenarioMaker().when_call_get_email_confirmation(
    ).then_response_should_be_a_redirect_to_app_deeplink_with_params()
def when_call_get_email_confirmation(self):...
client = Client()
self.response = client.get('{}?{}'.format(reverse(
    'email-confirmation-redirect'), 'token=ABXZ'))
return self
