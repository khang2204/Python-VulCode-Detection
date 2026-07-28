def r_augment(children):...
for entry in children:
if entry['submittable']:
entry.update({'submission_count': 0, 'submissions': [], 'best_submission':
    None, 'points': 0, 'passed': entry['points_to_pass'] == 0, 'graded': 
    False, 'unofficial': False})
r_augment(entry.get('children'))
