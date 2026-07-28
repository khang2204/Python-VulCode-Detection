def t_STRETCH2(t):...
"""docstring"""
t.value = beamr.interpreters.Stretch(t.value[1] + t.value[-2], t.value[2:-2])
return t
