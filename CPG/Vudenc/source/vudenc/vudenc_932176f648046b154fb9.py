def __getType(self, value):...
t = type(value)
if t is str:
return 'TEXT'
if t is bool:
return 'BOOLEAN'
if t is int:
return 'DOUBLE PRECISION'
if t is float:
return 'DOUBLE PRECISION'
if t is list:
t2 = type(value[0])
if t2 is str:
return 'TEXT[]'
if t2 is bool:
return 'BOOLEAN[]'
if t2 is int:
return 'DOUBLE PRECISION[]'
if t2 is float:
return 'DOUBLE PRECISION[]'
