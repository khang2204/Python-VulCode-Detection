def build_conditions(self):...
self.conditions = []
self.grouped_or_conditions = []
self.build_filter_conditions(self.filters, self.conditions)
self.build_filter_conditions(self.or_filters, self.grouped_or_conditions)
if not self.flags.ignore_permissions:
match_conditions = self.build_match_conditions()
if match_conditions:
self.conditions.append('(' + match_conditions + ')')
