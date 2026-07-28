def error_msg(self, message: str, delim=None, format=None, replace=False):...
"""docstring"""
if delim is None:
delim = ': '
if format:
message = format_lazy(message, **format)
if replace:
self.message = message
assert 'message' not in self.__dict__, 'You are calling error_msg without replace=True after calling it with it firts. Fix your code by removing firts method call add replace=True to second method call too.'
self.message = string_concat(self.message, delim, message)
