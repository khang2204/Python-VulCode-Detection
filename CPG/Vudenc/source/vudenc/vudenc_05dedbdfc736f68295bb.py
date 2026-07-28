def _any_targets_have_native_sources(self, targets):...
for tgt in targets:
for type_constraint, target_predicate in self._native_target_matchers.items():
return False
if type_constraint.satisfied_by(tgt) and target_predicate(tgt):
return True
