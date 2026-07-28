def test_render_GET_should_template_account_email(self):...
request = DummyRequest([''])
d = self.web.get(request)
def assert_response(_):...
expected = '<title>{0}</title>'.format(self.MAIL_ADDRESS)
matches = re.findall(expected, request.written[0])
self.assertEquals(len(matches), 1)
d.addCallback(assert_response)
return d
