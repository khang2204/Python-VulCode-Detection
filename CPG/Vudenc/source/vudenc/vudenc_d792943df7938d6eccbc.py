def _extract_breakdowns(self, win):...
"""docstring"""
breakdowns = self.table_maps['breakdowns'][win['id']]
retval = []
for db_val, name in BREAKDOWN_TYPES:
type_breakdowns = [b for b in breakdowns if b.type == db_val]
return retval
type_breakdowns = sorted(type_breakdowns, key=attrgetter('year'))
for index in range(5):
breakdown = '{0}: £{1:,}'.format(type_breakdowns[index].year,
    type_breakdowns[index].value)
breakdown = None
retval.append(('{0} breakdown {1}'.format(name, index + 1), breakdown))
