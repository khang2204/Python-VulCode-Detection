"""
Created on 1 Feb 2018

@author: Teodor Gherasim Nistor
"""
from ply import lex
from beamr.lexers.generic import t_error
from beamr.lexers.document import t_COMMENT
import beamr
tokens = ('COMMENT', 'ESCAPE', 'STRETCH1', 'STRETCH2', 'EMPH', 'CITATION',
    'FOOTNOTE', 'URL', 'LISTITEM', 'COLUMN', 'IMGENV', 'PLUSENV', 'TABENV',
    'VERBATIM', 'MACRO', 'BOX', 'ANTIESCAPE', 'TEXT')
def t_ESCAPE(t):...
"""docstring"""
t.value = beamr.interpreters.Escape(t.value)
return t
