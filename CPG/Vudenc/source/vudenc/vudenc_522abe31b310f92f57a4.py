def post_error(botobj, e):...
self.assertEqual(self.server, botobj._remote)
lines = e.splitlines()
self.assertEqual('Jumping out of the loop', lines[0])
self.assertEqual('Traceback (most recent call last):', lines[1])
