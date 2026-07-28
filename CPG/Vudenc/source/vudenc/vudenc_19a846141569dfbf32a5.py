def shell_first(command: str) ->str:...
"""docstring"""
cmd = shlex.split(command)
return subprocess.check_output(cmd).decode('utf-8').split('\n')[0]
