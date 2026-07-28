def handleBoolOp(item, stack, symbols, symId):...
params = []
for i in range(item[1]):
p = stack.pop()
if len(params) == 1:
if p >= 0:
if params[0] < 0:
if params[0] >= 0 and params[1] >= 0:
params.insert(0, int(p, 16))
params.insert(0, p)
func = boolMapSym[item[0]]
func = boolMap[item[0]]
func = boolMap[item[0]]
func = boolMapSym[item[0]]
stack.append(func(params, symbols, symId))
stack.append(helpers.toHex(func(params)))
stack.append(helpers.toHex(func(params)))
stack.append(func(params, symbols, symId))
