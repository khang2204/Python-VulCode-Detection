def test_terminate_assertion_consumer_service(self):...
eppn = 'hubba-bubba'
def _check():...
self.assertIn('reauthn-for-termination', session)
then = session['reauthn-for-termination']
now = int(time.time())
self.assertTrue(now - then < 5)
self.acs('/terminate', eppn, _check)
