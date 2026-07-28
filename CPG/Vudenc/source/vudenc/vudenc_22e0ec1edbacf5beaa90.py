def t_FOOTNOTE(t):...
"""docstring"""
t.value = beamr.interpreters.Footnote(t.value[2:-2])
return t
