@auth.autologin...
items = models.ErrorReportingMonitoring.query().fetch()
items.sort(key=lambda x: x.created_ts)
params = {'silenced': items, 'xsrf_token': self.generate_xsrf_token()}
self.response.out.write(template.render('ereporter2/silence.html', params))
