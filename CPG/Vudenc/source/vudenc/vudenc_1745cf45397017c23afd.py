def _get_active_nsp(self, hostname):...
"""docstring"""
result = self.common._cli_run('showvlun -a -host %s' % hostname, None)
if result:
result = result[1:]
for line in result:
info = line.split(',')
if info and len(info) > 4:
return info[4]
