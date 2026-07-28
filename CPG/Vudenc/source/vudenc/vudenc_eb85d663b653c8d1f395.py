def t_CITATION(t):...
"""docstring"""
t.value = beamr.interpreters.Citation(t.value[3:-1])
return t
