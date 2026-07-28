def get_processor_cores(self):...
ret, output = shellutil.run_get_output("sysctl hw.ncpu |awk '{print $2}'")
if ret:
return int(output)
