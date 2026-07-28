def targets(self, predicate=None, **kwargs):...
"""docstring"""
target_set = self._collect_targets(self.target_roots, **kwargs)
synthetics = OrderedSet()
for synthetic_address in self.build_graph.synthetic_addresses:
if self.build_graph.get_concrete_derived_from(synthetic_address) in target_set:
target_set.update(self._collect_targets(synthetics, **kwargs))
synthetics.add(self.build_graph.get_target(synthetic_address))
return list(filter(predicate, target_set))
