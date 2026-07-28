def param1Simple(op, params, symbols, symId):...
if params[0] < 0:
p0 = symbols[params[0]]
p0 = params[0]
x = SymbolicInput(symId[0], op, p0, None)
symbols[symId[0]] = x
symId[0] -= 1
return x.getId()
