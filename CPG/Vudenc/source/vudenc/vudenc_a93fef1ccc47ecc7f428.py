def test_bad_with_no_prior_key(self):...
"""docstring"""
config.set(xsrf_token_key=None)
tool = utils.XsrfTool()
timestamp = utils.get_timestamp(XsrfToolTests.TEST_NOW)
self.assertFalse(tool.verify_token('NotTheRightDigest/%f' % timestamp, 
    12345, 'test_action'))
