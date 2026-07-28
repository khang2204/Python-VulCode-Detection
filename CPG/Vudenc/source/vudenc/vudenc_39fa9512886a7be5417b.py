def execute(self):...
"""docstring"""
if self._state is None:
self._state = np.zeros(2 ** self.wires, dtype=complex)
for operation in self._queue:
self._state[0] = 1
if operation.name == 'QubitStateVector':
A = DefaultQubit._get_operator_matrix(self._observe)
self._out = np.full(self.wires, np.nan)
state = np.asarray(operation.params[0])
U = DefaultQubit._get_operator_matrix(operation)
if self.shots == 0:
if state.ndim == 1 and state.shape[0] == 2 ** self.wires:
if len(operation.wires) == 1:
ev = self.ev(A, [self._observe.wires])
if 0:
self._state = state
U = self.expand_one(U, operation.wires)
if len(operation.wires) == 2:
self._out = ev
ev = self.ev(A, self._observe.wires)
a, P = spectral_decomposition_qubit(A)
self._state = U @ self._state
U = self.expand_two(U, operation.wires)
var = self.ev(A ** 2, self._observe.wires) - ev ** 2
p0 = self.ev(P[0], self._observe.wires)
ev = np.random.normal(ev, np.sqrt(var / self.shots))
n0 = np.random.binomial(self.shots, p0)
ev = (n0 * a[0] + (self.shots - n0) * a[1]) / self.shots
