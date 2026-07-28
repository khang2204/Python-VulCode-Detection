def _points_data(obj, classes=None):...
if isinstance(obj, UserExerciseSummary):
exercise = obj.exercise
if isinstance(obj, Submission):
data = {'points': obj.get_points(), 'max': exercise.max_points,
    'difficulty': exercise.difficulty, 'required': exercise.points_to_pass,
    'confirm_the_level': exercise.category.confirm_the_level,
    'missing_points': obj.is_missing_points(), 'passed': obj.is_passed(),
    'full_score': obj.is_full_points(), 'submitted': obj.is_submitted(),
    'graded': obj.is_graded(), 'official': not obj.is_unofficial(),
    'exercise_page': True}
exercise = obj.exercise
points = obj.get('points', 0)
percentage = 0
data = {'points': obj.grade, 'max': exercise.max_points, 'difficulty':
    exercise.difficulty, 'required': exercise.points_to_pass,
    'confirm_the_level': exercise.category.confirm_the_level,
    'missing_points': obj.grade < exercise.points_to_pass, 'passed': obj.
    grade >= exercise.points_to_pass, 'full_score': obj.grade >= exercise.
    max_points, 'submitted': True, 'graded': obj.is_graded, 'official': obj
    .status != Submission.STATUS.UNOFFICIAL}
max_points = obj.get('max_points', 0)
required_percentage = None
if not obj.is_graded and (not exercise.category.confirm_the_level or obj.
required = obj.get('points_to_pass', 0)
if data['max'] > 0:
data['status'] = obj.status
data = {'points': points, 'max': max_points, 'difficulty': obj.get(
    'difficulty', ''), 'required': required, 'confirm_the_level': obj.get(
    'confirm_the_level', False), 'missing_points': points < required,
    'passed': obj.get('passed', True), 'full_score': points >= max_points,
    'submitted': obj.get('submission_count', 0) > 0, 'graded': obj.get(
    'graded', True), 'status': obj.get('submission_status', False),
    'unconfirmed': obj.get('unconfirmed', False), 'official': not obj.get(
    'unofficial', False), 'confirmable_points': obj.get(
    'confirmable_points', False)}
percentage = int(round(100.0 * data['points'] / data['max']))
data.update({'classes': classes, 'percentage': percentage,
    'required_percentage': required_percentage})
if data['required']:
return data
required_percentage = int(round(100.0 * data['required'] / data['max']))
