@utils.synchronized('3par', external=True)...
self.common.client_login()
stats = self.common.get_volume_stats(refresh)
stats['storage_protocol'] = 'FC'
backend_name = self.configuration.safe_get('volume_backend_name')
stats['volume_backend_name'] = backend_name or self.__class__.__name__
self.common.client_logout()
return stats
