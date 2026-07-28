def _get_token(self):...
"""docstring"""
resp = self.session.get(self.login_url)
token = re.findall('_xsrf=([\\w|-]+)', resp.headers.get('Set-Cookie'))[0]
return token
