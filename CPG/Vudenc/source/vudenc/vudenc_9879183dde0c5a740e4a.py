def assert_response(_):...
expected = '<title>{0}</title>'.format(self.MAIL_ADDRESS)
matches = re.findall(expected, request.written[0])
self.assertEquals(len(matches), 1)
