"""
Created on 1 Feb 2018

@author: Teodor Gherasim Nistor
"""
from beamr.debug import debug, warn
from beamr.lexers import docLexer, slideLexer
from beamr.parsers import docParser, slideParser
from beamr.interpreters import Config, VerbatimEnv
def __init__(self, children, before='', after='', inter=''):...
self.children = children
self.before = before
self.after = after
self.inter = inter
def __str__(self):...
s = self.before
for c in self.children:
s += str(c) + self.inter
s += self.after
return s
