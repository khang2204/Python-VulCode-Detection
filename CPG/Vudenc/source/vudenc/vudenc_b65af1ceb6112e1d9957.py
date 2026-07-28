def when_call_login_email_redirect(self):...
client = Client()
self.response = client.get('{}?{}'.format(reverse('login-redirect'),
    'token=ABXZ'))
return self
