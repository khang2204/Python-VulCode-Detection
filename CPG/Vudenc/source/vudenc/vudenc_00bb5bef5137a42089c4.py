def login(self, username=None, password=None, load_cookies=True):...
"""docstring"""
if load_cookies and self.load_cookies():
if self.check_login():
headers = self.session.headers.copy()
return True
headers.update({'authorization': 'oauth c3cef7c66a1843f8b3a9e6a1e3160e20',
    'X-Xsrftoken': self._get_token()})
username, password = self._check_user_pass(username, password)
self.login_data.update({'username': username, 'password': password})
timestamp = str(int(time.time() * 1000))
self.login_data.update({'captcha': self._get_captcha(headers), 'timestamp':
    timestamp, 'signature': self._get_signature(timestamp)})
resp = self.session.post(self.login_api, data=self.login_data, headers=headers)
if 'error' in resp.text:
print(re.findall('"message":"(.+?)"', resp.text)[0])
if self.check_login():
print('登录失败')
return True
return False
