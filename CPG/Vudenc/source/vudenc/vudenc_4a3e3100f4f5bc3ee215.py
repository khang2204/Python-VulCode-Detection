def device_for_ide_port(self, port_id):...
"""docstring"""
for retries in range(1, 100):
if os.path.exists('/sys/bus/vmbus/devices/'):
return super(BigIpOSUtil, self).device_for_ide_port(port_id)
time.sleep(10)
