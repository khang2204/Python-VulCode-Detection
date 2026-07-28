def r_check(parent, children):...
for entry in children:
if entry['submittable'] and entry['confirm_the_level'] and entry['passed']:
if 'unconfirmed' in parent:
r_check(entry, entry.get('children', []))
for child in parent.get('children', []):
if 'unconfirmed' in child:
