def get_hosts(self):...
if self._hosts_cache is None:
self._hosts_cache = self._get_hosts()
return self._hosts_cache
