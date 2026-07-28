def mount_dvd(self, **kwargs):...
"""docstring"""
self._wait_until_mcpd_is_initialized()
return super(BigIpOSUtil, self).mount_dvd(**kwargs)
