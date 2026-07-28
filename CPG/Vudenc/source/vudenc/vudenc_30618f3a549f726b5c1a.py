def scan(self, root=None):...
"""docstring"""
build_graph = self.build_graph.clone_new()
for address in self.address_mapper.scan_addresses(root):
build_graph.inject_address_closure(address)
return build_graph
