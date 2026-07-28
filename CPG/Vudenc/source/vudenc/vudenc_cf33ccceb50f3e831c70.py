def ltgt(op, params, symbols, symId):...
if params[0] < 0:
p0 = symbols[params[0]]
p0 = params[0]
if params[1] < 0:
makeUnsigned256(p0)
p1 = symbols[params[1]]
p1 = params[1]
x = SymbolicInput(symId[0], op, p0, p1)
makeUnsigned256(p1)
symbols[symId[0]] = x
symId[0] -= 1
return x.getId()
