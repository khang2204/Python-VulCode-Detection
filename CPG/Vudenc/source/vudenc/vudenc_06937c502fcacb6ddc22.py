def delete_snapshot(self, snapshot):...
"""docstring"""
self._eql_execute('volume', 'select', snapshot['volume_name'], 'snapshot',
    'delete', snapshot['name'])
LOG.error(_('Failed to delete snapshot %(snap)s of volume %(vol)s'), {
    'snap': snapshot['name'], 'vol': snapshot['volume_name']})
