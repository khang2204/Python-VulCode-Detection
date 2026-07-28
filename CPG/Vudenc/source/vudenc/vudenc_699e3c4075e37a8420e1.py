@auth.autologin...
error = models.Error.get_by_id(int(error_id))
if not error:
self.abort(404, 'Error not found')
params = {'error': error, 'now': utils.utcnow()}
self.response.out.write(template.render('ereporter2/error.html', params))
