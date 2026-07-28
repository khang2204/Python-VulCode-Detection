@property...
"""docstring"""
combinations = set()
for f, f_ in zip(self.output, self.rule.output):
if f in self.dynamic_output:
wildcards = defaultdict(list)
for f, w in self.expand_dynamic(f_, restriction=self.wildcards, omit_value=
for combination in combinations:
combinations.add(tuple(w.items()))
for name, value in combination:
return wildcards
wildcards[name].append(value)
