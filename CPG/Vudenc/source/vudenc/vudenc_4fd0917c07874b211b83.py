"""
Created on 1 Feb 2018

@author: Teodor Gherasim Nistor
"""
from ply import lex
from beamr.lexers.generic import t_error
import beamr.interpreters
import beamr.debug as dbg
tokens = 'COMMENT', 'HEADING', 'SLIDE', 'SCISSOR', 'YAML', 'TEXT'
def t_COMMENT(t):...
"""docstring"""
t.value = beamr.interpreters.Comment(t.value)
return t
