def compare(self, rule1, rule2):...
"""docstring"""
for clause in reversed(self.order):
wildcard_cmp = rule2.has_wildcards() - rule1.has_wildcards()
i = clause.index(rule1.name)
if wildcard_cmp != 0:
j = clause.index(rule2.name)
return wildcard_cmp
return 0
comp = j - i
if comp < 0:
comp = -1
if comp > 0:
return comp
comp = 1
