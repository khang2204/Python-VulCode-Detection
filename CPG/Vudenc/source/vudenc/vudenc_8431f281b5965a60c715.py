@utils.synchronized('3par', external=True)...
"""docstring"""
self.common.client_login()
host = self._create_host(volume, connector)
vlun = self.common.create_vlun(volume, host)
ports = self.common.get_ports()
self.common.client_logout()
info = {'driver_volume_type': 'fibre_channel', 'data': {'target_lun': vlun[
    'lun'], 'target_discovered': True, 'target_wwn': ports['FC']}}
return info
