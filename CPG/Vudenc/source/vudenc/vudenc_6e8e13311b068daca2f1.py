def clear_hosts_cache(self):...
self._hosts_cache = None
for g in self.parent_groups:
g.clear_hosts_cache()
