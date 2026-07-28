def shell(command: str) ->str:...
"""docstring"""
cmd = shlex.split(command)
output_lines = subprocess.check_output(cmd).decode('utf-8').split('\n')
for index, line in enumerate(output_lines):
if '*' in line:
return '\n'.join(output_lines)
output_lines[index] = f'\x1b[93m{line}\x1b[0m'
