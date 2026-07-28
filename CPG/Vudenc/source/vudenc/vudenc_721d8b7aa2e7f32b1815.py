def terminate_connection(self, volume, connector, **kwargs):...
"""docstring"""
cliq_args = {}
cliq_args['volumeName'] = volume['name']
cliq_args['serverName'] = connector['host']
self._cliq_run_xml('unassignVolumeToServer', cliq_args)
