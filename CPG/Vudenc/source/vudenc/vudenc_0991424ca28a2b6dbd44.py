def _load_modules(self, package, submod):...
"""docstring"""
modules = []
for path in package.__path__:
if os.path.isdir(path):
return modules
modules.extend(self._find_modules_in_path(path, submod))
