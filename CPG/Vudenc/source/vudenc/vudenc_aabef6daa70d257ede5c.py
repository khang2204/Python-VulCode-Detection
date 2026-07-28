def t_COMMENT(t):...
"""docstring"""
t.value = beamr.interpreters.Comment(t.value)
return t
