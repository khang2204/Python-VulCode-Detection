@utils.synchronized('3par', external=True)...
self.common.client_login()
new_vol = self.common.create_cloned_volume(volume, src_vref)
self.common.client_logout()
return {'metadata': new_vol}
