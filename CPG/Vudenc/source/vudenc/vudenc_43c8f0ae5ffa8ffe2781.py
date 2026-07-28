def hermitian(*args):...
"""docstring"""
A = np.asarray(args[0])
if A.shape[0] != A.shape[1]:
if not np.allclose(A, A.conj().T, atol=tolerance):
return A
