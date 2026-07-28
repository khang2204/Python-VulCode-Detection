def handleDupOp(op, symbols, stack, symId):...
num = int(op[3:])
val = stack[-num]
if val < 0:
sym = symbols[val]
stack.append(val)
x = SymbolicInput(symId[0], 'Dup', sym)
symbols[symId[0]] = x
symId[0] -= 1
