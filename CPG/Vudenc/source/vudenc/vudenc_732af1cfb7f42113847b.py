def handle_login(self):...
pwd = self.parser.require('cppwd', 64)
if not pwd in self.auth.iuser:
h = [u'Set-Cookie: cppwd=x; path=/; expires=Thu, 01 Jan 1970 00:00:00 GMT']
h = ['Set-Cookie: cppwd={}; Path=/'.format(pwd)]
self.loud_reply(u'bad_ppwd "{}"'.format(pwd), headers=h)
self.loud_reply(u'login_ok', headers=h)
