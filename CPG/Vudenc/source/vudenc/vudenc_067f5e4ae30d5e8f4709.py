def get(self, error=''):...
xsrf_token = self.xsrf_from_html()
params = {'error_info': error, 'xsrf_token': xsrf_token}
body = self.wrap_html('templates/register.html', params)
return self.write(body)
