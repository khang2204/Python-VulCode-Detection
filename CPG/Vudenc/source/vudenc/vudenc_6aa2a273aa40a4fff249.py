def client_disconnect(self, csessid):...
"""docstring"""
if csessid in self.requests:
self.requests[csessid].finish()
if csessid in self.databuffer:
