def get_leaf_nodes(self):...
leafs = []
for n in self.nodes:
if len(self.get_dependencies(n['node_object'])) < 1:
return leafs
leafs.append(n)
