def __init__(self, spdx):...
self.spdx = spdx
self.lasttok = None
self.lastid = None
self.lexer = lex.lex(module=self, reflags=re.UNICODE)
self.parser = yacc.yacc(module=self, write_tables=False, debug=False)
self.lines_checked = 0
self.checked = 0
self.spdx_valid = 0
self.spdx_errors = 0
self.curline = 0
self.deepest = 0
