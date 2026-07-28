def check_executables(executables=None):...
if executables is None:
executables = REQUIRED_EXECUTABLES
mdeps = []
for exe, pkg in executables:
return mdeps
check_executable(exe, pkg)
mdeps.append(e)
