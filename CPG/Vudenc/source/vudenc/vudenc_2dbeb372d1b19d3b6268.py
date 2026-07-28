def check(self):...
for clause in self._ruleorder:
for rulename in clause:
if not self.is_rule(rulename):
