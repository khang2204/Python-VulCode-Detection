def _parse_poly(self, pstr, var):...
pstr = ''.join(map(str.strip, pstr))
summands = pstr.split('+')
coefficients = list(map(lambda x: self._parse_coeff(x, var), summands))
cs = [0] * (max(degree for _, degree in coefficients) + 1)
for value, degree in coefficients:
if degree < 0:
return cs
if self.degree_limit is not None and degree > self.degree_limit:
cs[degree] = value
