def get_attributes(self, levelfields, doc):...
attributes = set()
rulenames = levelfields['rules']
for rulename in rulenames:
rule = doc['rules'][rulename]
return attributes
attributes |= get_rule_attributes(rule, doc)
