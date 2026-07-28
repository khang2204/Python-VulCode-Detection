def get_dependencies(self, obj, label=None):...
antecedents = []
this_ord = self.find_ord(obj)
for node, dep, lbl in self.edges:
if label:
return antecedents
if node == this_ord and lbl == label:
if node == this_ord:
antecedents.append(self.nodes[dep])
antecedents.append(self.nodes[dep])
