def test_token_login_old_user(self):...
eppn = 'hubba-bubba'
shared_key = self.app.config['TOKEN_LOGIN_SHARED_KEY']
timestamp = '{:x}'.format(int(time.time()))
nonce = os.urandom(16).encode('hex')
token = sha256('{0}|{1}|{2}|{3}'.format(shared_key, eppn, nonce, timestamp)
    ).hexdigest()
data = {'eppn': eppn, 'token': token, 'nonce': nonce, 'ts': timestamp}
resp = c.post('/token-login', data=data)
self.assertEqual(resp.status_code, 302)
self.assertTrue(resp.location.startswith(self.app.config[
    'TOKEN_LOGIN_FAILURE_REDIRECT_URL']))
