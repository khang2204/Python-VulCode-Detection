def list_rules(self, only_targets=False):...
rules = self.rules
if only_targets:
rules = filterfalse(Rule.has_wildcards, rules)
for rule in rules:
logger.rule_info(name=rule.name, docstring=rule.docstring)
