def test_poll_server_sleep(self):...
slept = []
bit = threading.Event()
self.mock(bit, 'wait', slept.append)
self.mock(bot_main, 'run_manifest', self.fail)
self.mock(bot_main, 'update_bot', self.fail)
self.expected_requests([(
    'https://localhost:1/auth/api/v1/accounts/self/xsrf_token', {'data': {},
    'headers': {'X-XSRF-Token-Request': '1'}}, {'xsrf_token': 'token'}), (
    'https://localhost:1/swarming/api/v1/bot/poll', {'data': self.
    attributes, 'headers': {'X-XSRF-Token': 'token'}}, {'cmd': 'sleep',
    'duration': 1.24})])
self.assertFalse(bot_main.poll_server(self.bot, bit))
self.assertEqual([1.24], slept)
