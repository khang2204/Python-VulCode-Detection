def _collect(self, client):...
"""docstring"""
if not client.local:
self.log_error('Error running sosreport: %s' % err)
client.sosreport()
if not self.config['no_local']:
if client.retrieved:
client.sosreport()
self.retrieved += 1
