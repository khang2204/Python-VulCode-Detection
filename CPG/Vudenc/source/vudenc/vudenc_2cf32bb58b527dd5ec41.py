def t_VERBATIM(t):...
"""docstring"""
gd = lexer.lexmatch.groupdict()
t.value = beamr.interpreters.VerbatimEnv(gd['VBTM_HEAD'].strip(), gd[
    'VBTM_BODY'])
return t
