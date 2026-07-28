def test_good_with_no_prior_key(self):...
"""docstring"""
config.set(xsrf_token_key=None)
tool = utils.XsrfTool()
token = tool.generate_token(12345, 'test_action')
self.assertTrue(tool.verify_token(token, 12345, 'test_action'))
