def get_rule(self, name):...
"""docstring"""
if not self._rules:
if not name in self._rules:
return self._rules[name]
