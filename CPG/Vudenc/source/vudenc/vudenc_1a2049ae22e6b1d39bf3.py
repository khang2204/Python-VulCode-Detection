def flush_profile_data(self):...
"""docstring"""
events = self.events
self.events = []
if self.worker.mode == ray.WORKER_MODE:
component_type = 'worker'
component_type = 'driver'
self.worker.raylet_client.push_profile_events(component_type, ray.UniqueID(
    self.worker.worker_id), self.worker.node_ip_address, events)
