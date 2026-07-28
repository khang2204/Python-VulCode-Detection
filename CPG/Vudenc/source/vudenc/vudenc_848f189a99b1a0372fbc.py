def render_targets(self, record):...
if record is not None:
targets = [injection_.target for injection_ in injection.objects.filter(
    result=record.id)]
targets = []
for index in range(len(targets)):
if targets[index] is None:
if len(targets) > 0:
targets[index] = '-'
return ', '.join(targets)
return '-'
