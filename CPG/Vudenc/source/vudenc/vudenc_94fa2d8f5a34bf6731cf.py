def get_volume_stats(self, refresh):...
if refresh:
self._update_backend_status()
return self.device_stats
