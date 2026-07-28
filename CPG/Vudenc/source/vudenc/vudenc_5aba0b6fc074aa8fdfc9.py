def ensure_export(self, context, volume):...
"""docstring"""
self._check_volume(volume)
LOG.warn(_('Volume %s is not found!, it may have been deleted'), volume['name']
    )
LOG.error(_('Failed to ensure export of volume %s'), volume['name'])
