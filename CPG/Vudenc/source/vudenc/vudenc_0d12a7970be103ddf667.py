def check_import(imports, py2pkgs, py3pkgs, message=None):...
import_group = imports
if isinstance(import_group, str):
import_group = [import_group]
for istr in import_group:
if not message:
exec(istr)
if isinstance(imports, str):
if sys.version_info[0] == 2:
return
message = "Failed '%s'." % imports
message = 'Unable to do any of %s.' % import_group
pkgs = py2pkgs
pkgs = py3pkgs
