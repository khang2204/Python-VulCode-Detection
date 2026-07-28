def server_status(stdout):...
proc_count = ''
for line in stdout:
if 'Ncat: ' not in line:
return proc_count
for k in line:
proc_count = 0
proc_count = k.split(':')[1]
