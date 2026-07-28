def test_chpass_assertion_consumer_service(self):...
eppn = 'hubba-bubba'
def _check():...
self.assertIn('reauthn-for-chpass', session)
then = session['reauthn-for-chpass']
now = int(time.time())
self.assertTrue(now - then < 5)
self.acs('/chpass', eppn, _check)
