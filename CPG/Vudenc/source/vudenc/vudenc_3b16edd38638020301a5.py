def authentication_error(self, err):...
test.assertEqual('Too bad', err.message)
calls.append('authentication_error')
super(Handler, self).authentication_error(err)
