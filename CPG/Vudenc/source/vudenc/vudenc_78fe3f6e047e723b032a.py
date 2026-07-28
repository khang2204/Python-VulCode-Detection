def execute(self):...
"""docstring"""
if self.eng:
self.eng.reset()
self.eng, q = sf.Engine(self.wires, hbar=self.hbar)
self.reset()
for operation in self._queue:
if operation.name not in operator_map:
self.state = self.eng.run('fock', cutoff_dim=self.cutoff)
p = [(x.val if isinstance(x, Variable) else x) for x in operation.params]
reg = self._observe.wires
op = operator_map[operation.name](*p)
if self._observe.name == 'Fock':
if isinstance(operation.wires, int):
ex = self.state.mean_photon(reg)
if self._observe.name == 'X':
op | q[operation.wires]
op | [q[i] for i in operation.wires]
var = 0
ex, var = self.state.quad_expectation(reg, 0)
if self._observe.name == 'P':
if self.shots != 0:
ex, var = self.state.quad_expectation(reg, np.pi / 2)
if self._observe.name == 'Homodyne':
ex = np.random.normal(ex, np.sqrt(var / self.shots))
self._out = ex
ex, var = self.state.quad_expectation(reg, *self.observe.params)
