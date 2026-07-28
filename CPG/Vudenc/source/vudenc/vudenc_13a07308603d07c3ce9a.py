def _update_volume_stats(self):...
"""docstring"""
LOG.debug(_('Updating volume stats'))
data = {}
backend_name = 'eqlx'
if self.configuration:
backend_name = self.configuration.safe_get('volume_backend_name')
data['volume_backend_name'] = backend_name or 'eqlx'
data['vendor_name'] = 'Dell'
data['driver_version'] = self.VERSION
data['storage_protocol'] = 'iSCSI'
data['reserved_percentage'] = 0
data['QoS_support'] = False
data['total_capacity_gb'] = 'infinite'
data['free_capacity_gb'] = 'infinite'
for line in self._eql_execute('pool', 'select', self.configuration.
if line.startswith('TotalCapacity:'):
self._stats = data
out_tup = line.rstrip().partition(' ')
if line.startswith('FreeSpace:'):
data['total_capacity_gb'] = self._get_space_in_gb(out_tup[-1])
out_tup = line.rstrip().partition(' ')
data['free_capacity_gb'] = self._get_space_in_gb(out_tup[-1])
