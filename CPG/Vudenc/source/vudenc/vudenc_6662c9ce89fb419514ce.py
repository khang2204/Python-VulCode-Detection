def test_rejects_expired_token(self):...
"""docstring"""
config.set(xsrf_token_key='abcdef')
tool = utils.XsrfTool()
token = tool.generate_token(12345, 'test_action')
utils.set_utcnow_for_test(XsrfToolTests.TEST_NOW + datetime.timedelta(hours
    =4, minutes=1))
self.assertFalse(tool.verify_token(token, 12345, 'test_action'))
