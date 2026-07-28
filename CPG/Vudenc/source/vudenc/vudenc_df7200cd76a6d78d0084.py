def then_response_should_be_a_redirect_to_app_deeplink_with_params(self):...
assert self.response.status_code == 302
assert self.response['Location'] == '{}{}?token=ABXZ'.format(settings.
    APP_DEEPLINK_DOMAIN, '/people/me/login')
return self
