@utils.synchronized('3par', external=True)...
"""docstring"""
self.common.client_login()
metadata = self.common.create_volume_from_snapshot(volume, snapshot)
self.common.client_logout()
return {'metadata': metadata}
