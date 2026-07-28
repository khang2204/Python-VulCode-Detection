def t_ANTIESCAPE(t):...
"""docstring"""
t.value = beamr.interpreters.Text('\\' + t.value)
return t
