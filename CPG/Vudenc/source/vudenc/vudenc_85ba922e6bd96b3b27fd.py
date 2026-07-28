def test_poll_server_run(self):...
manifest = []
bit = threading.Event()
self.mock(bit, 'wait', self.fail)
self.mock(bot_main, 'run_manifest', lambda *args: manifest.append(args))
self.mock(bot_main, 'update_bot', self.fail)
self.expected_requests([(
    'https://localhost:1/auth/api/v1/accounts/self/xsrf_token', {'data': {},
    'headers': {'X-XSRF-Token-Request': '1'}}, {'xsrf_token': 'token'}), (
    'https://localhost:1/swarming/api/v1/bot/poll', {'data': self.bot.
    _attributes, 'headers': {'X-XSRF-Token': 'token'}}, {'cmd': 'run',
    'manifest': {'foo': 'bar'}})])
self.assertTrue(bot_main.poll_server(self.bot, bit))
expected = [(self.bot, {'foo': 'bar'}, time.time())]
self.assertEqual(expected, manifest)
