def run(self):...
if self.options['inference']:
self._run_pre_inference(self.target_graph)
shapes = find_shapes(self.shacl_graph)
results = {}
for s in shapes:
r = s.validate(self.target_graph)
return results
results[s.node] = r
