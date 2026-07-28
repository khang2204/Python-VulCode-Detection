def clone(self):...
"""docstring"""
new_obj = type(self)()
new_obj.charset = self.charset
if self._parts:
new_obj._parts = list(self._parts)
new_obj._path = self._path
new_obj._leading_slash = self._leading_slash
return new_obj
new_obj._trailing_slash = self._trailing_slash
