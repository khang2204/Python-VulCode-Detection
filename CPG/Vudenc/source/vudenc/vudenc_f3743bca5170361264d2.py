def _deallocate3(self):...
"""docstring"""
if self.eng is not None and self.backend == 'Simulator' or self.backend == 'IBMBackend':
self.eng.flush()
self.eng.backend.collapse_wavefunction(self.reg, [(0) for i in range(len(
    self.reg))])
