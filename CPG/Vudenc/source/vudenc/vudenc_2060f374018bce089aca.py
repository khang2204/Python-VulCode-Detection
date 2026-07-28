def signExtend(params, symbols, symId=-1):...
x = params[0]
i = params[1]
sign_bit = 1 << i - 1
return (x & sign_bit - 1) - (x & sign_bit)
