def makeJump(x, symbols, symId):...
sym = symbols[x]
newSym = SymbolicInput(symId[0], 'Not', sym)
symbols[symId[0]] = newSym
symId[0] -= 1
