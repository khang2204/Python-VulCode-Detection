def expand_one(self, U, wires):...
"""docstring"""
if U.shape != (2, 2):
if len(wires) != 1:
wires = wires[0]
before = 2 ** wires
after = 2 ** (self.wires - wires - 1)
U = np.kron(np.kron(np.eye(before), U), np.eye(after))
return U
