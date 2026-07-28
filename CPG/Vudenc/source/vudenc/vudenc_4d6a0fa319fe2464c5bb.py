def symbAdrJump(condition, address, symbols, items, symId):...
sym = symbols[condition]
x = SymbolicInput(symId[0], 'IsZero', sym, address)
symbols[symId[0]] = x
symId[0] -= 1
return (x.getId(), jumpToLoc(address, items)), -1
