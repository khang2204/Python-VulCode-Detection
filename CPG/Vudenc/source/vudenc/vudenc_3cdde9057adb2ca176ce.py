def _get_least_used_nsp(self, nspss):...
"""docstring"""
result = self.common._cli_run('showvlun -a -showcols Port', None)
nsp_counts = {}
for nsp in nspss:
nsp_counts[nsp] = 0
current_least_used_nsp = None
if result:
result = result[1:]
return current_least_used_nsp
for line in result:
nsp = line.strip()
current_smallest_count = sys.maxint
if nsp in nsp_counts:
for nsp, count in nsp_counts.iteritems():
nsp_counts[nsp] = nsp_counts[nsp] + 1
if count < current_smallest_count:
current_least_used_nsp = nsp
current_smallest_count = count
