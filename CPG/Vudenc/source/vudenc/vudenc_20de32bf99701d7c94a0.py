def get_total_mem(self):...
cmd = "sysctl hw.physmem |awk '{print $2}'"
ret, output = shellutil.run_get_output(cmd)
if ret:
return int(output) / 1024 / 1024
