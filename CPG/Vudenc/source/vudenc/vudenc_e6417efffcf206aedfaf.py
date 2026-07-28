def __eq__(self, other):...
if not isinstance(other, Host):
return False
return self._uuid == other._uuid
