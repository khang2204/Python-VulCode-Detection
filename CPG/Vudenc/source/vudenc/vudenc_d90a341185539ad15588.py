def _update_backend_status(self):...
data = {}
backend_name = self.configuration.safe_get('volume_backend_name')
data['volume_backend_name'] = backend_name or self.__class__.__name__
data['driver_version'] = '1.0'
data['reserved_percentage'] = 0
data['storage_protocol'] = 'iSCSI'
data['vendor_name'] = 'Hewlett-Packard'
result_xml = self._cliq_run_xml('getClusterInfo', {})
cluster_node = result_xml.find('response/cluster')
total_capacity = cluster_node.attrib.get('spaceTotal')
free_capacity = cluster_node.attrib.get('unprovisionedSpace')
GB = 1073741824
data['total_capacity_gb'] = int(total_capacity) / GB
data['free_capacity_gb'] = int(free_capacity) / GB
self.device_stats = data
