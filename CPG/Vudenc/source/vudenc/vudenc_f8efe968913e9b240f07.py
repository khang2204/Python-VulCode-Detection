@utils.synchronized('3par', external=True)...
self.common.client_login()
self.common.create_snapshot(snapshot)
self.common.client_logout()
