import helpers
import ophandlers
import oplists
from copy import deepcopy
def __init__(self, opcodes, functions, stack=[], memory=[], storage={},...
self.opcodes = opcodes
self.functions = functions
self.stack = stack
self.memory = memory
self.storage = storage
self.symbols = symbols
self.userIn = userIn
self.instrPtr = instrPtr
self.symId = symId
def takeJumpPath(self, pair, symbols):...
self.instrPtr = pair[1][0]
return ophandlers.makeJump(pair[0], symbols, self.symId)
