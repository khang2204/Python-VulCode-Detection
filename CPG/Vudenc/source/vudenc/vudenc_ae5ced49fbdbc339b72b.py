def run(self, description):...
if description and len(description) > 500:
c.errors.add(errors.DESC_TOO_LONG)
return unkeep_space(description or '')
