def _deallocate2(self):...
"""docstring"""
if self.eng is not None and self.backend == 'Simulator' or self.backend == 'IBMBackend':
for qubit in self.reg:
self.eng.deallocate_qubit(qubit)
