@staticmethod...
if callable(gl_type):
retval = BaseHandler.validate_python_type(value, gl_type)
if isinstance(gl_type, collections.Mapping):
if not retval:
retval = BaseHandler.validate_jmessage(value, gl_type)
if isinstance(gl_type, str):
log.err('-- Invalid python_type, in [%s] expected %s' % (value, gl_type))
return retval
if not retval:
retval = BaseHandler.validate_GLtype(value, gl_type)
if isinstance(gl_type, collections.Iterable):
log.err('-- Invalid JSON/dict [%s] expected %s' % (value, gl_type))
return retval
if not retval:
if len(value) == 0:
log.err('-- Failed Match in regexp [%s] against %s' % (value, gl_type))
return retval
return True
retval = all(BaseHandler.validate_type(x, gl_type[0]) for x in value)
if not retval:
log.err('-- List validation failed [%s] of %s' % (value, gl_type))
return retval
