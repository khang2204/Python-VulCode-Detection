def ev(self, A, wires):...
"""docstring"""
if A.shape != (2, 2):
A = self.expand_one(A, wires)
expectation = np.vdot(self._state, A @ self._state)
if np.abs(expectation.imag) > tolerance:
log.warning('Nonvanishing imaginary part {} in expectation value.'.format(
    expectation.imag))
return expectation.real
