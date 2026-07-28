def t_SCISSOR(t):...
"""docstring"""
t.value = beamr.interpreters.ScissorEnv(t.value[3:-1])
return t
