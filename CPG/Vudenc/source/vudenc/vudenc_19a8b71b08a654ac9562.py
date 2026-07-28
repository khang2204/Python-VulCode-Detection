def create_snapshot(self, snapshot):...
"""docstring"""
out = self._eql_execute('volume', 'select', snapshot['volume_name'],
    'snapshot', 'create-now')
LOG.error(_('Failed to create snapshot of volume %s'), snapshot['volume_name'])
prefix = 'Snapshot name is '
snap_name = self._get_prefixed_value(out, prefix)
self._eql_execute('volume', 'select', snapshot['volume_name'], 'snapshot',
    'rename', snap_name, snapshot['name'])
