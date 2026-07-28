def _get_iscsi_ip(self, hostname):...
"""docstring"""
if len(self.iscsi_ips) == 1:
return self.iscsi_ips.keys()[0]
nsp = self._get_active_nsp(hostname)
if nsp is None:
nsp = self._get_least_used_nsp(self._get_iscsi_nsps())
return self._get_ip_using_nsp(nsp)
if nsp is None:
msg = _('Least busy iSCSI port not found, using first iSCSI port in list.')
LOG.warn(msg)
return self.iscsi_ips.keys()[0]
