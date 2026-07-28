def node(x, y, z):...
qm.RX(x, [0])
qm.CNOT([0, 1])
qm.RY(-1.6, [0])
qm.RY(y, [1])
qm.CNOT([1, 0])
qm.RX(z, [0])
qm.CNOT([0, 1])
qm.expectation.Hermitian(np.array([[0, 1], [1, 0]]), 0)
