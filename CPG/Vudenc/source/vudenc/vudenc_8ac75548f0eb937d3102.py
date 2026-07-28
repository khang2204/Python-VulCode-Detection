def get_lines(command: str) ->List[str]:...
"""docstring"""
stdout = get_output(command)
return [line.strip().decode() for line in stdout.splitlines()]
