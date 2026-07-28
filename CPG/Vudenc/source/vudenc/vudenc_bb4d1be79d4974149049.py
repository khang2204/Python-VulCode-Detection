def _get_iscsi_nsps(self):...
"""docstring"""
nsps = []
for value in self.iscsi_ips.values():
nsps.append(value['nsp'])
return nsps
