def poll_server(botobj, _):...
sleep_streak = botobj.state['sleep_streak']
self.assertEqual(botobj.remote, self.server)
if sleep_streak == 5:
return False
