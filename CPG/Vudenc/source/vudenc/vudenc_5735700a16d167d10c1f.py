def test_post_error_task(self):...
self.mock(time, 'time', lambda : 126.0)
self.mock(logging, 'error', lambda *_, **_kw: None)
self.mock(bot_main, 'get_remote', lambda : self.server)
self.mock(os_utilities, 'get_state', lambda : {'foo': 'bar'})
expected_attribs = bot_main.get_attributes(None)
self.expected_requests([(
    'https://localhost:1/auth/api/v1/accounts/self/xsrf_token', {'data':
    expected_attribs, 'headers': {'X-XSRF-Token-Request': '1'}}, {
    'xsrf_token': 'token'}), (
    'https://localhost:1/swarming/api/v1/bot/task_error/23', {'data': {'id':
    expected_attribs['dimensions']['id'][0], 'message': 'error', 'task_id':
    23}, 'headers': {'X-XSRF-Token': 'token'}}, {})])
botobj = bot_main.get_bot()
bot_main.post_error_task(botobj, 'error', 23)
