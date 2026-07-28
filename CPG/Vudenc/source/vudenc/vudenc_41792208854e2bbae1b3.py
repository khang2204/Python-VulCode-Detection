def expand_two(self, U, wires):...
"""docstring"""
if U.shape != (4, 4):
if len(wires) != 2:
wires = np.asarray(wires)
if np.any(wires < 0) or np.any(wires >= self.wires) or wires[0] == wires[1]:
a = np.min(wires)
b = np.max(wires)
n_between = b - a - 1
before = 2 ** a
after = 2 ** (self.wires - b - 1)
between = 2 ** n_between
U = np.kron(U, np.eye(between))
if wires[0] < wires[1]:
p = [0, 2, 1]
p = [1, 2, 0]
dim = [2, 2, between]
p = np.array(p)
perm = np.r_[p, p + 3]
temp = np.prod(dim)
U = U.reshape(dim * 2).transpose(perm).reshape([temp, temp])
U = np.kron(np.kron(np.eye(before), U), np.eye(after))
return U
