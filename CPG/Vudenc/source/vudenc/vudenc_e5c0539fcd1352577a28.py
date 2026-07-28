@utils.synchronized('3par', external=True)...
self.common.client_login()
self.common.delete_snapshot(snapshot)
self.common.client_logout()
