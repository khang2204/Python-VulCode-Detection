def report_error(exc_type, value, tb):...
import traceback
logger.critical('Exception: %s' % ''.join(traceback.format_exception(
    exc_type, value, tb)))
if hasattr(sys, 'ps1'):
print(''.join(traceback.format_exception(exc_type, value, tb)))
rollbar.report_exc_info((exc_type, value, tb))
