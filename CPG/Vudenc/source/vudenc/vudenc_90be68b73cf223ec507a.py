def unitary(*args):...
"""docstring"""
U = np.asarray(args[0])
if U.shape[0] != U.shape[1]:
if not np.allclose(U @ U.conj().T, np.identity(U.shape[0]), atol=tolerance):
return U
