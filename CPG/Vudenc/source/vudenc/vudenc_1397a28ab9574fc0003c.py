def initialize_connection(self, volume, connector):...
"""docstring"""
self._create_server(connector)
cliq_args = {}
cliq_args['volumeName'] = volume['name']
cliq_args['serverName'] = connector['host']
self._cliq_run_xml('assignVolumeToServer', cliq_args)
iscsi_properties = self._get_iscsi_properties(volume)
return {'driver_volume_type': 'iscsi', 'data': iscsi_properties}
