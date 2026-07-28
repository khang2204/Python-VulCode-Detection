def find_libs(self, names):...
"""docstring"""
def collect_existing_libs():...
def lib_paths():...
yield os.path.join(self.home, 'lib')
if self.jdk:
yield os.path.join(self.home, 'jre', 'lib')
for name in names:
for path in lib_paths():
return list(collect_existing_libs())
lib_path = os.path.join(path, name)
if os.path.exists(lib_path):
yield lib_path
