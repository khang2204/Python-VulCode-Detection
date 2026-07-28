def signedDiv(params, symbols, symId=-1):...
x = params[0]
y = params[1]
if not y:
return y
if x == -2 ** 255 and y == -1:
return -2 ** 255
return copysign(abs(x / y), x / y)
