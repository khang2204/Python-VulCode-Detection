def get_root_nodes(self):...
roots = []
for n in self.nodes:
if len(self.get_dependents(n['node_object'])) < 1:
return roots
roots.append(n)
