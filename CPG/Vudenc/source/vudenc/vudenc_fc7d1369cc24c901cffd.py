def _get_hosts(self):...
hosts = []
seen = {}
for kid in self.child_groups:
kid_hosts = kid.get_hosts()
for mine in self.hosts:
for kk in kid_hosts:
if mine not in seen:
return hosts
if kk not in seen:
seen[mine] = 1
seen[kk] = 1
if self.name == 'all' and mine.implicit:
if self.name == 'all' and kk.implicit:
hosts.append(mine)
hosts.append(kk)
