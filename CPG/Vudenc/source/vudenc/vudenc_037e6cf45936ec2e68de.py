def bin_paths():...
yield self._bin_path
if self._is_jdk:
yield os.path.join(self.home, 'jre', 'bin')
