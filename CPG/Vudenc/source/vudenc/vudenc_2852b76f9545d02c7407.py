def add_rule(self, name=None, lineno=None, snakefile=None):...
"""docstring"""
if name is None:
name = str(len(self._rules) + 1)
if self.is_rule(name):
rule = Rule(name, self, lineno=lineno, snakefile=snakefile)
self._rules[rule.name] = rule
self.rule_count += 1
if not self.first_rule:
self.first_rule = rule.name
return name
