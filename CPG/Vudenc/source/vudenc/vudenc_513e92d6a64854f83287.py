def find_case(cname, ename, cases):...
for c in cases:
if c.check.name == cname and c.environ.name == ename:
return c
