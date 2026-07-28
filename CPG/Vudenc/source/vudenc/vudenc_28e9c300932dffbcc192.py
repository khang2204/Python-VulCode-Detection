def get_rules_as_json(mapping):...
rules = getattr(mapping, 'rules', None)
if rules:
rules = json.dumps(rules, indent=4)
return safestring.mark_safe(rules)
