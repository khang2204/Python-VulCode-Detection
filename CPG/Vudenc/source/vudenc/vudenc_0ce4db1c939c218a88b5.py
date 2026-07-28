def sysctl(command):...
"""docstring"""
out = subprocess.check_output(command)
result = out.split(b' ')[1]
return int(result)
return result
