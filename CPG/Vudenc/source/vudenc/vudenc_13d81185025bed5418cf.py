@app.exception(Exception)...
title = None
help = None
if isinstance(exception, NotFound):
status = 404
if isinstance(exception, InvalidUsage):
info = {}
status = 405
if isinstance(exception, DatasetteError):
message = exception.args[0]
info = {}
status = exception.status
status = 500
templates = ['500.html']
message = exception.args[0]
info = exception.error_dict
info = {}
if status != 500:
message = exception.message
message = str(exception)
templates = ['{}.html'.format(status)] + templates
info.update({'ok': False, 'error': message, 'status': status, 'title': title})
if exception.messagge_is_html:
traceback.print_exc()
if request is not None and request.path.split('?')[0].endswith('.json'):
message = Markup(message)
title = exception.title
return response.json(info, status=status)
template = self.jinja_env.select_template(templates)
return response.html(template.render(info), status=status)
