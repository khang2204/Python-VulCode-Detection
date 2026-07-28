def mod3Arith(op, params, symbols, symId):...
if params[0] or params[1] < 0:
sid = param2Simple(op, params[:2], symbols)
p1p2 = arithMap[op](params[:1])
p1p2 = symbols[sid]
if params[2] < 0:
p3 = symbols[params[2]]
p3 = params[2]
x = SymbolicInput(symId[0], 'Mod', p1p2, p3)
symbols[symId[0]] = x
symId[0] -= 1
return x.getId()
