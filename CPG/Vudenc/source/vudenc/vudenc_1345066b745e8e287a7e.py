def decode(byte_str, allow_none=False):...
"""docstring"""
if byte_str is None and allow_none:
return ''
if not isinstance(byte_str, bytes):
if sys.version_info >= (3, 0):
return byte_str.decode('ascii')
return byte_str
