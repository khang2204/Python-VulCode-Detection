@utils.synchronized('3par', external=True)...
self.common.client_login()
self.common.delete_volume(volume)
self.common.client_logout()
