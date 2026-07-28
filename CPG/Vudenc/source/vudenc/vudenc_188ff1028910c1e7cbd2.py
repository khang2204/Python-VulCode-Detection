def _get_ip_using_nsp(self, nsp):...
"""docstring"""
for key, value in self.iscsi_ips.items():
if value['nsp'] == nsp:
return key
