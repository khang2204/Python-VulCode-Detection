def handle_exception(self, exception, _):...
"""docstring"""
status = 500
self.handle_exception_exception()
values = {'message': exception.message, 'email': helpers.get_user_email(),
    'traceDump': traceback.format_exc(), 'status': status, 'type':
    exception.__class__.__name__}
if isinstance(exception, helpers.EarlyExitException):
status = exception.status
values['params'] = self.request.params.dict_of_lists()
values = exception.to_dict()
if status >= 400 and status <= 499:
logging.info(json.dumps(values, cls=JsonEncoder))
logging.exception(exception)
if helpers.should_render_json(self.request.headers.get('accept', ''), self.
self.render_json(values, status)
if status == 403 or status == 401:
self.render_forbidden(exception.message)
self.render('error.html', values, status)
