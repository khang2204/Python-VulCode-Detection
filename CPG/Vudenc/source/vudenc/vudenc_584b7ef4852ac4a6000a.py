def injectables(self, build_graph):...
if self.version == 'custom':
return
specs_to_create = [('scalac', self._create_compiler_jardep), (
    'scala-library', self._create_runtime_jardep)]
for spec_key, create_jardep_func in specs_to_create:
spec = self.injectables_spec_for_key(spec_key)
target_address = Address.parse(spec)
if not build_graph.contains_address(target_address):
jars = [create_jardep_func(self.version)]
if not build_graph.get_target(target_address).is_synthetic:
build_graph.inject_synthetic_target(target_address, JarLibrary, jars=jars,
    scope='forced')
