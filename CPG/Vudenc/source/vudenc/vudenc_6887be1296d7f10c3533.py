def _validated_executable(self, name):...
exe = self._validated_binaries.get(name)
if not exe:
exe = self._validate_executable(name)
return exe
self._validated_binaries[name] = exe
