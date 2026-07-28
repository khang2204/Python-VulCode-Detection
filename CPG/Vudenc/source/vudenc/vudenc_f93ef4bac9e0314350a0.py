def _generate_data(self, instance, user, data=None):...
data = deepcopy(self.content.data)
module_index = data['module_index']
exercise_index = data['exercise_index']
modules = data['modules']
categories = data['categories']
total = data['total']
def r_augment(children):...
for entry in children:
if entry['submittable']:
for module in modules:
entry.update({'submission_count': 0, 'submissions': [], 'best_submission':
    None, 'points': 0, 'passed': entry['points_to_pass'] == 0, 'graded': 
    False, 'unofficial': False})
r_augment(entry.get('children'))
module.update({'submission_count': 0, 'points': 0, 'points_by_difficulty':
    {}, 'unconfirmed_points_by_difficulty': {}, 'passed': module[
    'points_to_pass'] == 0})
for entry in categories.values():
r_augment(module['children'])
entry.update({'submission_count': 0, 'points': 0, 'points_by_difficulty': {
    }, 'unconfirmed_points_by_difficulty': {}, 'passed': entry[
    'points_to_pass'] == 0})
total.update({'submission_count': 0, 'points': 0, 'points_by_difficulty': {
    }, 'unconfirmed_points_by_difficulty': {}})
if user.is_authenticated():
submissions = user.userprofile.submissions.exclude_errors().filter(
    exercise__course_module__course_instance=instance).prefetch_related(
    'exercise').only('id', 'exercise', 'submission_time', 'status', 'grade')
def r_check(parent, children):...
for submission in submissions:
for entry in children:
tree = self._by_idx(modules, exercise_index[submission.exercise.id])
self.dirty = True
entry = tree[-1]
if entry['submittable'] and entry['confirm_the_level'] and entry['passed']:
for module in modules:
entry['submission_count'] += 1 if not submission.status in (Submission.
    STATUS.ERROR, Submission.STATUS.UNOFFICIAL) else 0
if 'unconfirmed' in parent:
r_check(entry, entry.get('children', []))
r_check(module, module['children'])
def add_to(target, entry):...
unofficial = submission.status == Submission.STATUS.UNOFFICIAL
for child in parent.get('children', []):
target['submission_count'] += entry['submission_count']
entry['submissions'].append({'id': submission.id, 'max_points': entry[
    'max_points'], 'points_to_pass': entry['points_to_pass'],
    'confirm_the_level': entry.get('confirm_the_level', False),
    'submission_count': 1, 'points': submission.grade, 'graded': submission
    .is_graded, 'passed': submission.grade >= entry['points_to_pass'],
    'submission_status': submission.status if not submission.is_graded else
    False, 'unofficial': unofficial, 'date': submission.submission_time,
    'url': submission.get_url('submission-plain')})
if 'unconfirmed' in child:
if entry.get('unofficial', False):
if submission.status == Submission.STATUS.READY and (entry['unofficial'] or
if entry.get('unconfirmed', False):
def r_collect(module, parent, children):...
entry.update({'best_submission': submission.id, 'points': submission.grade,
    'passed': not unofficial and submission.grade >= entry['points_to_pass'
    ], 'graded': submission.status == Submission.STATUS.READY, 'unofficial':
    unofficial})
if submission.notifications.count() > 0:
self._add_by_difficulty(target['unconfirmed_points_by_difficulty'], entry[
    'difficulty'], entry['points'])
target['points'] += entry['points']
passed = True
entry['notified'] = True
self._add_by_difficulty(target['points_by_difficulty'], entry['difficulty'],
    entry['points'])
max_points = 0
if submission.notifications.filter(seen=False).count() > 0:
submissions = 0
entry['unseen'] = True
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
