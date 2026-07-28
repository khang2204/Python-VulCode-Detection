def test_gen_and_verify_good_token(self):...
"""docstring"""
config.set(xsrf_token_key='abcdef')
tool = utils.XsrfTool()
token = tool.generate_token(12345, 'test_action')
self.assertTrue(tool.verify_token(token, 12345, 'test_action'))
