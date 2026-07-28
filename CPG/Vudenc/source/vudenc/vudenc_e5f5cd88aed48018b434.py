def create_cloned_volume(self, volume, src_vref):...
"""docstring"""
src_volume_name = self.configuration.volume_name_template % src_vref['id']
LOG.error(_('Failed to create clone of volume %s'), volume['name'])
out = self._eql_execute('volume', 'select', src_volume_name, 'clone',
    volume['name'])
return self._get_volume_data(out)
