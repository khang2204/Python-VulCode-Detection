def evaluate(self, target_graph, value_nodes):...
"""docstring"""
fails = []
for f in value_nodes:
t = target_graph.objects(f, RDF_type)
if len(fails) > 0:
for ctype in iter(t):
return False, fails
return True, None
if ctype == self.class_rule:
fails.append(f)
subclasses = target_graph.objects(ctype, RDFS_subClassOf)
if self.class_rule in iter(subclasses):
