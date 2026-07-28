def traverse(self, pathSymbols):...
gasCost = 0
stop = False
while not stop:
if self.instrPtr == 2:
pathSymbols.append(self.symbols)
item = self.opcodes[self.instrPtr]
return []
op = item[0]
if op in oplists.terminalOps:
if op in oplists.arithOps:
ophandlers.handleArithOps(item, self.stack, self.symbols, self.symId)
if op in oplists.boolOps:
self.instrPtr = item[-1]
ophandlers.handleBoolOp(item, self.stack, self.symbols, self.symId)
if op == 'SHA3':
stop = self.instrPtr >= len(self.opcodes)
if op in oplists.envOps:
ophandlers.handleEnvOps(item, self.stack, self.memory, self.symbols, self.
    userIn, self.symId)
if op in oplists.blockOps:
ophandlers.handleBlockOps(item, self.stack, self.symbols)
if op in oplists.jumpOps:
result = ophandlers.handleJumpOps(op, self.stack, self.opcodes, self.
    symbols, self.symId)
if op in oplists.memOps:
if result[0] != -1 and result[1] != -1:
ophandlers.handleMemoryOps(item, self.stack, self.memory, self.symbols)
if op in oplists.storOps:
self.instrPtr, stop = result
if result[1] == -1:
ophandlers.handleStorageOps(item, self.stack, self.storage, self.symbols,
    self.userIn)
if op == 'JUMPDEST':
self.instrPtr = item[-1]
if op == 'POP':
ep1 = ExecutionPath(self.opcodes, self.functions, self.stack[:], self.
    memory[:], deepcopy(self.storage), deepcopy(self.symbols), self.userIn[
    :], self.instrPtr)
self.stack.pop()
if op == 'PC':
stop = ep1.takeJumpPath(result[0], self.symbols)
self.stack.append(i)
if op[:4] == 'PUSH':
if stop:
self.stack.append(op[7:])
if op[:3] == 'DUP':
return [self]
print('splitting')
ophandlers.handleDupOp(op, self.symbols, self.stack, self.symId)
if op[:4] == 'SWAP':
return [self, ep1]
num = int(op[4:])
if op[:3] == 'LOG':
tmp = self.stack[-num]
self.stack[-num] = self.stack[-1]
self.stack[-1] = tmp
