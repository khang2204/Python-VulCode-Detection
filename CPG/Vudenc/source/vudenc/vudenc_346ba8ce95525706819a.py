def close_ssh_session(self):...
"""docstring"""
if self.local:
return True
self.client.close()
self.log_error('Error closing SSH session: %s' % e)
self.connected = False
return False
return True
