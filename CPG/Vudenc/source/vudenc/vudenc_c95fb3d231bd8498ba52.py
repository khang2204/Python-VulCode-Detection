def t_EMPH(t):...
"""docstring"""
gd = lexer.lexmatch.groupdict()
t.value = beamr.interpreters.Emph(gd['EMPH_FLAG'], gd['EMPH_TXT'])
return t
