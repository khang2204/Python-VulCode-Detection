import helpers
import ctypes
from symbolicinput import SymbolicInput
from math import copysign
def handleJumpOps(op, stack, items, symbols, symId):...
adr = stack.pop()
out = -1, False
if op == 'JUMP':
return jumpToLoc(adr, items)
if op == 'JUMPI':
cond = stack.pop()
return out
if cond > 0:
return jumpToLoc(adr, items)
if cond < 0:
return symbAdrJump(cond, adr, symbols, items, symId)
