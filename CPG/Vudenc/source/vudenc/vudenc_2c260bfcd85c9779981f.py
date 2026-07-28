def error_handle(error=None):...
if error is None:
error = sys.exc_info()[0]
if DEBUG:
logger.error(error)
return error
return 'Unexpected error'
