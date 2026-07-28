def create_volume(self, volume):...
"""docstring"""
cliq_args = {}
cliq_args['clusterName'] = self.configuration.san_clustername
if self.configuration.san_thin_provision:
cliq_args['thinProvision'] = '1'
cliq_args['thinProvision'] = '0'
cliq_args['volumeName'] = volume['name']
if int(volume['size']) == 0:
cliq_args['size'] = '100MB'
cliq_args['size'] = '%sGB' % volume['size']
self._cliq_run_xml('createVolume', cliq_args)
volume_info = self._cliq_get_volume_info(volume['name'])
cluster_name = volume_info['volume.clusterName']
iscsi_iqn = volume_info['volume.iscsiIqn']
cluster_interface = '1'
if not self.cluster_vip:
self.cluster_vip = self._cliq_get_cluster_vip(cluster_name)
iscsi_portal = self.cluster_vip + ':3260,' + cluster_interface
model_update = {}
model_update['provider_location'] = '%s %s %s' % (iscsi_portal, iscsi_iqn, 0)
return model_update
