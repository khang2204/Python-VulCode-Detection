def t_URL(t):...
"""docstring"""
t.value = beamr.interpreters.Url(t.value[1:-1])
return t
