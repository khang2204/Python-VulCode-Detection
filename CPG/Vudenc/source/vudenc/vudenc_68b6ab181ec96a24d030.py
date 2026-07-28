def remove_group(self, group):...
if group in self.groups:
self.groups.remove(group)
for oldg in group.get_ancestors():
if oldg.name != 'all':
for childg in self.groups:
if oldg in childg.get_ancestors():
