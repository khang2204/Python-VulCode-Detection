def _parse_instruction(self, s):...
match = self.divex.match(s)
if match is None:
poly1 = match.group(1)
poly2 = match.group(2)
instruction = 'mod'
p = int(match.group(3))
var = match.group(4)
cs1 = self._parse_poly(poly1, var)
cs2 = self._parse_poly(poly2, var)
field = polylib.IntField(p)
p1 = polylib.FieldPoly(field, cs1)
p2 = polylib.FieldPoly(field, cs2)
return p1, instruction, p2
