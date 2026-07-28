def test_run_bot(self):...
self.mock(time, 'time', lambda : 126.0)
def poll_server(botobj, _):...
sleep_streak = botobj.state['sleep_streak']
self.assertEqual(botobj.remote, self.server)
if sleep_streak == 5:
return False
