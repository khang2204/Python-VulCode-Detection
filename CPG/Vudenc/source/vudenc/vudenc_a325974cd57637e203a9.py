@staticmethod...
"""docstring"""
if isinstance(value, (str, unicode)):
return bool(re.match(gl_type, value))
return False
