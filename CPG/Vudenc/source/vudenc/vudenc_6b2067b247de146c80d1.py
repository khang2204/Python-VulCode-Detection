def _validate_executable(self, name):...
def bin_paths():...
yield self._bin_path
if self._is_jdk:
yield os.path.join(self.home, 'jre', 'bin')
for bin_path in bin_paths():
exe = os.path.join(bin_path, name)
if self._is_executable(exe):
return exe
