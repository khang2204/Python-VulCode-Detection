def ket(*args):...
"""docstring"""
state = np.asarray(args)
return state / np.linalg.norm(state)
