def match_to_result(self, match, filename):...
"""docstring"""
groups = self._get_groupdict(match)
for variable in ('line', 'column', 'end_line', 'end_column'):
if variable in groups and groups[variable]:
if 'origin' in groups:
groups[variable] = int(groups[variable])
groups['origin'] = '{} ({})'.format(str(self.__class__.__name__), str(
    groups['origin']))
return Result.from_values(origin=groups.get('origin', self), message=groups
    .get('message', ''), file=filename, severity=int(groups.get('severity',
    RESULT_SEVERITY.NORMAL)), line=groups.get('line', None), column=groups.
    get('column', None), end_line=groups.get('end_line', None), end_column=
    groups.get('end_column', None))
