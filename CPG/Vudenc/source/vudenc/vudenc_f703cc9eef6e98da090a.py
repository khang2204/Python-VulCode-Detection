def _check():...
self.assertIn('reauthn-for-chpass', session)
then = session['reauthn-for-chpass']
now = int(time.time())
self.assertTrue(now - then < 5)
