def get(self, error=''):...
self.check()
params = {'error_info': error, 'name': self.email, 'xsrf_token': self.
    xsrf_from_html()}
body = self.wrap_html('templates/pwdchange.html', params)
return self.write(body)
