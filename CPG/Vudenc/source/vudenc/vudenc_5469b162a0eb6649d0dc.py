def dependents(self, on_predicate=None, from_predicate=None):...
"""docstring"""
core = set(self.targets(on_predicate))
dependees = defaultdict(set)
for target in self.targets(from_predicate):
for dependency in target.dependencies:
return dependees
if dependency in core:
dependees[target].add(dependency)
