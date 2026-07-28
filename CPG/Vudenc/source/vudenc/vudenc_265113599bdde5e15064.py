@classmethod...
"""docstring"""
if A.name not in operator_map:
if not callable(operator_map[A.name]):
return operator_map[A.name]
p = [(x.val if isinstance(x, Variable) else x) for x in A.params]
return operator_map[A.name](*p)
