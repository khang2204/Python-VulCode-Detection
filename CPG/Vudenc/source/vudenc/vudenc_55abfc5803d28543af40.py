def vmstat(stat):...
"""docstring"""
out = subprocess.check_output(['vmstat', '-s'])
stat = stat.encode('ascii')
for line in out.split(b'\n'):
line = line.strip()
if stat in line:
return int(line.split(b' ')[0])
