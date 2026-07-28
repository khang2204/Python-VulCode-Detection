def _cliq_get_volume_info(self, volume_name):...
"""docstring"""
cliq_args = {}
cliq_args['volumeName'] = volume_name
result_xml = self._cliq_run_xml('getVolumeInfo', cliq_args)
volume_attributes = {}
volume_node = result_xml.find('response/volume')
for k, v in volume_node.attrib.items():
volume_attributes['volume.' + k] = v
status_node = volume_node.find('status')
if status_node is not None:
for k, v in status_node.attrib.items():
permission_node = volume_node.find('permission')
volume_attributes['status.' + k] = v
if permission_node is not None:
for k, v in status_node.attrib.items():
LOG.debug(_('Volume info: %(volume_name)s => %(volume_attributes)s') % {
    'volume_name': volume_name, 'volume_attributes': volume_attributes})
volume_attributes['permission.' + k] = v
return volume_attributes
