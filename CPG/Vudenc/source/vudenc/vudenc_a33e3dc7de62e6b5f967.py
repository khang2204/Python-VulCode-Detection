@contextmanager...
exe = self._validate_executable(name)
yield exe
self._validated_binaries[name] = exe
