def _check():...
self.assertIn('reauthn-for-termination', session)
then = session['reauthn-for-termination']
now = int(time.time())
self.assertTrue(now - then < 5)
