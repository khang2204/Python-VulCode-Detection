def when_call_get_email_confirmation(self):...
client = Client()
self.response = client.get('{}?{}'.format(reverse(
    'email-confirmation-redirect'), 'token=ABXZ'))
return self
