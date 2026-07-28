def handleArithOps(item, stack, symbols, symId):...
params = []
for i in range(item[1]):
p = stack.pop()
if params[0] > 0 and params[1] > 0:
if p >= 0:
if len(params) == 3 and params[2] < 0:
func = arithMapSym[item[0]]
params.insert(0, int(p, 16))
params.insert(0, p)
func = arithMapSym[item[0]]
func = arithMap[item[0]]
stack.append(func(params, symbols, symId))
stack.append(func(params, symbols, symId))
stack.append(helpers.toHex(func(params)))
