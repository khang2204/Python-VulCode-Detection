@staticmethod...
"""docstring"""
if _sparse.issparse(A) == False:
w, pi = _sla.eigs(A, k=1, which='LM', ncv=lanczosVecs, maxiter=maxiter)
pi = pi.reshape(pi.size)
if normalized:
pi /= sum(pi)
return pi
