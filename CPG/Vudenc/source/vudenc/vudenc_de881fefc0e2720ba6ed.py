def get_dependents(self, obj, label=None):...
decendents = []
this_ord = self.find_ord(obj)
for node, dep, lbl in self.edges:
if label:
return decendents
if dep == this_ord and lbl == label:
if dep == this_ord:
decendents.append(self.nodes[node])
decendents.append(self.nodes[node])
