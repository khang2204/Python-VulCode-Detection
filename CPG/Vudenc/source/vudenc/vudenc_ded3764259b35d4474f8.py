def __load_exercisecollection(self, request):...
user = self.profile.user
if user.is_authenticated():
self.exercise.check_submission(user, no_update=True)
target_exercises = []
for t_exercise in self.exercise.exercises:
it = t_exercise.parent
title = '{}: {} - {}'.format(t_exercise.course_module.course_instance.
    course.name, t_exercise.course_module.course_instance.instance_name,
    t_exercise.category.name)
ex_url = it.url
return target_exercises, title
it = it.parent
while it is not None:
ex_url = it.url + '/' + ex_url
ex_name = t_exercise.name
it = it.parent
for candidate in t_exercise.name.split('|'):
if request.LANGUAGE_CODE in candidate:
data = {'exercise': t_exercise, 'url': reverse('exercise', kwargs={
    'course_slug': t_exercise.course_module.course_instance.course.url,
    'instance_slug': t_exercise.course_module.course_instance.url,
    'module_slug': t_exercise.course_module.url, 'exercise_path': ex_url}),
    'title': ex_name, 'max_points': t_exercise.max_points, 'user_points':
    UserExerciseSummary(t_exercise, request.user).get_points()}
ex_name = candidate[len('{}:'.format(request.LANGUAGE_CODE)):]
target_exercises.append(data)
