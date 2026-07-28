def signedMod(params, symbols, symId=-1):...
x = params[0]
y = params[1]
if y:
return copysign(abs(x) % abs(y), x)
return y
