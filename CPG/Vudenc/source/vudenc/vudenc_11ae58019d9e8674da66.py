def targets_from_witch(self):...
for t in d.witch_targets:
if t['domain'] == 'beon.ru' and t['forum'] == 'anonymous':
add_target_exc(t['id'], t['user'])
