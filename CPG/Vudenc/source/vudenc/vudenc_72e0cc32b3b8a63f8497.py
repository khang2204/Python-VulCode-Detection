def create_volume(self, volume):...
"""docstring"""
cmd = ['volume', 'create', volume['name'], '%sG' % volume['size']]
LOG.error(_('Failed to create volume %s'), volume['name'])
if self.configuration.eqlx_pool != 'default':
cmd.append('pool')
if self.configuration.san_thin_provision:
cmd.append(self.configuration.eqlx_pool)
cmd.append('thin-provision')
out = self._eql_execute(*cmd)
return self._get_volume_data(out)
