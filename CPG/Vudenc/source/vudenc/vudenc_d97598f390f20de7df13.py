"""
Created on 1 Feb 2018

@author: Teodor Gherasim Nistor
"""
import beamr.debug as debug
from beamr.parsers.generic import p_nil, p_error
from ply import yacc
from beamr.lexers.slide import tokens
start = 'main'
def p_main(t):...
"""docstring"""
if len(t) > 2:
t[0] = t[1]
t[0] = []
t[0].append(t[2])
def p_elem(t):...
"""docstring"""
t[0] = t[1]
parser = yacc.yacc(tabmodule='slide_parsetab', debugfile='slide_parsedbg',
    debug=not debug.quiet)
