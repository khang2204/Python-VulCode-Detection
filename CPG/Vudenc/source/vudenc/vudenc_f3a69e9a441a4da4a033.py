def _set_sos_prefix(self, prefix):...
"""docstring"""
if self.host.containerized:
prefix = prefix % {'image': self.config['image'] or self.host.container_image}
self.host.prefix = prefix
