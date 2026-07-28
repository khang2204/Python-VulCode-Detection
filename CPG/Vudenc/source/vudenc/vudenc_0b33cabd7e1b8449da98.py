def _get_ancestors(self):...
results = {}
for g in self.parent_groups:
results[g.name] = g
return results
results.update(g._get_ancestors())
