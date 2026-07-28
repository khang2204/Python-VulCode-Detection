@property...
"""docstring"""
if not self._home:
home = self._get_system_properties(self.java)['java.home']
return self._home
if os.path.basename(home) == 'jre':
jdk_dir = os.path.dirname(home)
self._home = home
if self._is_executable(os.path.join(jdk_dir, 'bin', 'javac')):
home = jdk_dir
