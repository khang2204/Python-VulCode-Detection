def _adb_grep_wrapper(self, adb_shell_cmd):...
"""docstring"""
return self._adb.shell(adb_shell_cmd).decode('utf-8')
if e.ret_code == 1 and not e.stdout and not e.stderr:
return False
