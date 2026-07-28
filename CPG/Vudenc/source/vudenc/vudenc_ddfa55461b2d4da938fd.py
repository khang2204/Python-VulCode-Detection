def check_imports(imports=None):...
if imports is None:
imports = REQUIRED_IMPORTS
mdeps = []
for import_str, py2pkg, py3pkg in imports:
return mdeps
check_import(import_str, py2pkg, py3pkg)
mdeps.append(e)
