def add_child_group(self, group):...
if self == group:
if group not in self.child_groups:
self.child_groups.append(group)
group.depth = max([self.depth + 1, group.depth])
group._check_children_depth()
if self.name not in [g.name for g in group.parent_groups]:
group.parent_groups.append(self)
self.clear_hosts_cache()
for h in group.get_hosts():
h.populate_ancestors()
