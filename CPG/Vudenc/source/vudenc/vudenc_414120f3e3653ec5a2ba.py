@utils.synchronized('3par', external=True)...
"""docstring"""
self.common.client_login()
host = self._create_host(volume, connector)
vlun = self.common.create_vlun(volume, host)
self.common.client_logout()
iscsi_ip = self._get_iscsi_ip(host['name'])
iscsi_ip_port = self.iscsi_ips[iscsi_ip]['ip_port']
iscsi_target_iqn = self.iscsi_ips[iscsi_ip]['iqn']
info = {'driver_volume_type': 'iscsi', 'data': {'target_portal': '%s:%s' %
    (iscsi_ip, iscsi_ip_port), 'target_iqn': iscsi_target_iqn, 'target_lun':
    vlun['lun'], 'target_discovered': True}}
return info
