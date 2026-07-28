@utils.synchronized('3par', external=True)...
self.common.client_login()
metadata = self.common.create_volume(volume)
self.common.client_logout()
return {'metadata': metadata}
