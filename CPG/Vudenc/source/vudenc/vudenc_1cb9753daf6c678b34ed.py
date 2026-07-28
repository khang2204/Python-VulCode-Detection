def run(self):...
"""docstring"""
self.subscribe(ray.gcs_utils.XRAY_HEARTBEAT_BATCH_CHANNEL)
self.subscribe(ray.gcs_utils.XRAY_DRIVER_CHANNEL)
while True:
self.update_local_scheduler_map()
if self.autoscaler:
self.autoscaler.update()
self._maybe_flush_gcs()
self.process_messages()
time.sleep(ray._config.heartbeat_timeout_milliseconds() * 0.001)
