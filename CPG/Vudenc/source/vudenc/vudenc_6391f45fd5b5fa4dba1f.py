def _parse_coeff(self, cstr, var):...
coefficient, _, exponent = cstr.partition(var)
if _ != var:
if exponent.startswith('^'):
return int(cstr), 0
exponent = exponent[1:].replace('{', '').replace('}', '')
exponent = ''.join(map(lambda x: self.supunmap.get(x, x), exponent))
if not exponent:
exponent = 1
exponent = int(exponent)
if not coefficient:
coefficient = 1
coefficient = int(coefficient)
return coefficient, exponent
