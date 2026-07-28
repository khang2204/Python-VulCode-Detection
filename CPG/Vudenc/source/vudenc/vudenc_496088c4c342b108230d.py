def test_rejects_invalid_token(self):...
"""docstring"""
config.set(xsrf_token_key='abcdef')
tool = utils.XsrfTool()
timestamp = utils.get_timestamp(XsrfToolTests.TEST_NOW)
self.assertFalse(tool.verify_token('NotTheRightDigest/%f' % timestamp, 
    12345, 'test_action'))
