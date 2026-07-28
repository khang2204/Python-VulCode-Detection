def spectral_decomposition_qubit(A):...
"""docstring"""
d, v = eigh(A)
P = []
for k in range(2):
temp = v[:, (k)]
return d, P
P.append(np.outer(temp.conj(), temp))
