def handleEnvOps(item, stack, memory, symbols, userIn, symId):...
params = []
for i in range(item[1]):
p = stack.pop()
if item[2] == 1:
if p >= 0:
x = SymbolicInput(symId[0], 'id', None)
params.insert(0, int(p, 16))
params.insert(0, p)
symbols[symId[0]] = x
stack.append(symId[0])
userIn.append(symId[0])
symId[0] -= 1
