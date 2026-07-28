def add_new_target(self, address, target_type, target_base=None,...
"""docstring"""
rel_target_base = target_base or address.spec_path
abs_target_base = os.path.join(get_buildroot(), rel_target_base)
if not os.path.exists(abs_target_base):
os.makedirs(abs_target_base)
if not self.source_roots.find_by_path(rel_target_base):
self.source_roots.add_source_root(rel_target_base)
if dependencies:
dependencies = [dep.address for dep in dependencies]
self.build_graph.inject_synthetic_target(address=address, target_type=
    target_type, dependencies=dependencies, derived_from=derived_from, **kwargs
    )
new_target = self.build_graph.get_target(address)
return new_target
