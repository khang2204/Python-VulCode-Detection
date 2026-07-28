@classmethod...
"""docstring"""
if cls._check_executable(executable):
if command is None:
return repr(executable) + ' is not installed.'
return True
check_call(command, stdout=DEVNULL, stderr=DEVNULL)
return fail_msg
return True
