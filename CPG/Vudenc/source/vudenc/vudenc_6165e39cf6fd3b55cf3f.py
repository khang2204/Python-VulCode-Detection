def test_poll_server_restart_load_test(self):...
os.environ['SWARMING_LOAD_TEST'] = '1'
bit = threading.Event()
self.mock(bit, 'wait', self.fail)
self.mock(bot_main, 'run_manifest', self.fail)
self.mock(bot_main, 'update_bot', self.fail)
self.mock(self.bot, 'restart', self.fail)
self.expected_requests([(
    'https://localhost:1/auth/api/v1/accounts/self/xsrf_token', {'data': {},
    'headers': {'X-XSRF-Token-Request': '1'}}, {'xsrf_token': 'token'}), (
    'https://localhost:1/swarming/api/v1/bot/poll', {'data': self.
    attributes, 'headers': {'X-XSRF-Token': 'token'}}, {'cmd': 'restart',
    'message': 'Please die now'})])
self.assertTrue(bot_main.poll_server(self.bot, bit))
