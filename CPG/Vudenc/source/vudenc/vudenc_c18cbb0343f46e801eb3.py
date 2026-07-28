def binary(self, name):...
"""docstring"""
if not isinstance(name, str):
self.validate()
return self._validated_executable(name)
