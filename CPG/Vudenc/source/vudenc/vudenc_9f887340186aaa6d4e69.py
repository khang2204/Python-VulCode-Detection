def r_collect(module, parent, children):...
passed = True
max_points = 0
submissions = 0
points = 0
confirm_entry = None
for entry in children:
if entry['submittable']:
if confirm_entry and submissions > 0:
if entry['confirm_the_level']:
passed = r_collect(module, entry, entry.get('children', [])) and passed
confirm_entry['confirmable_points'] = True
if parent and not parent['submittable']:
confirm_entry = entry
passed = passed and entry['passed']
parent['max_points'] = max_points
return passed
max_points += entry['max_points']
parent['submission_count'] = submissions
submissions += entry['submission_count']
parent['points'] = points
if entry['graded']:
points += entry['points']
add_to(module, entry)
add_to(categories[entry['category_id']], entry)
add_to(total, entry)
