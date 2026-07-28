@property...
"""docstring"""
for f, f_ in zip(self.output, self.rule.output):
if f in self.dynamic_output:
expansion = self.expand_dynamic(f_, restriction=self.wildcards, omit_value=
    _IOFile.dynamic_fill)
yield f
if not expansion:
yield f_
for f, _ in expansion:
yield IOFile(f, self.rule)
