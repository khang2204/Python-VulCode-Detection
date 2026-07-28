def delete_volume(self, volume):...
"""docstring"""
cliq_args = {}
cliq_args['volumeName'] = volume['name']
cliq_args['prompt'] = 'false'
volume_info = self._cliq_get_volume_info(volume['name'])
LOG.error('Volume did not exist. It will not be deleted')
self._cliq_run_xml('deleteVolume', cliq_args)
return
