def handle_exception_exception(self):...
"""docstring"""
exception = sys.exc_info()[1]
values = {'message': exception.message, 'traceDump': traceback.format_exc()}
logging.exception(exception)
if helpers.should_render_json(self.request.headers.get('accept', ''), self.
self.render_json(values, 500)
self.render('error.html', values, 500)
