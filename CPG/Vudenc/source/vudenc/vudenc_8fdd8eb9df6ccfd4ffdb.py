def get_parameters(self, levelfields, doc):...
parameters = set()
rulenames = levelfields['rules']
for rulename in rulenames:
rule = doc['rules'][rulename]
return parameters
parameters |= get_rule_parameters(rule, doc)
