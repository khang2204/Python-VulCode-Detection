def check_login(self):...
"""docstring"""
resp = self.session.get(self.login_url, allow_redirects=False)
if resp.status_code == 302:
self.session.cookies.save()
return False
print('登录成功')
return True
