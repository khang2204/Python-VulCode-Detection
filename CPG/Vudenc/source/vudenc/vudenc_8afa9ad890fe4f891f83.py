@auth.autologin...
data = logscraper._log_request_id(request_id)
if not data:
self.abort(404, detail='Request id was not found.')
self.response.write(template.render('ereporter2/request.html', {'request':
    data}))
