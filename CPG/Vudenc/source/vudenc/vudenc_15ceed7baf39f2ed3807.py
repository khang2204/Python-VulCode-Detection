def add_group(self, group):...
for oldg in group.get_ancestors():
if oldg not in self.groups:
if group not in self.groups:
self.add_group(oldg)
self.groups.append(group)
