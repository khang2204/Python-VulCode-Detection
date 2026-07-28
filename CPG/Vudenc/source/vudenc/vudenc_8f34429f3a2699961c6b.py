def _get_groupdict(self, match):...
"""docstring"""
groups = match.groupdict()
if isinstance(self.severity_map, dict) and 'severity' in groups and groups[
groups['severity'] = self.severity_map[groups['severity']]
return groups
