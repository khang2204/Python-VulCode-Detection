def _deallocate(self):...
"""docstring"""
if self.eng is not None and self.backend == 'Simulator' or self.backend == 'IBMBackend':
pq.ops.All(pq.ops.Measure) | self.reg
