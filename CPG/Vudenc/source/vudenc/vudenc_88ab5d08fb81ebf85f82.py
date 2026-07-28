def write_error(self, status_code, **kw):...
exception = kw.get('exception')
if exception and hasattr(exception, 'error_code'):
error_dict = {}
RequestHandler.write_error(self, status_code, **kw)
error_dict.update({'error_message': exception.reason, 'error_code':
    exception.error_code})
if hasattr(exception, 'arguments'):
error_dict.update({'arguments': exception.arguments})
error_dict.update({'arguments': []})
self.set_status(status_code)
self.finish(error_dict)
