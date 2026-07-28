def invalidate_content_m2m(sender, instance, action, reverse, model, pk_set,...
if action not in ('post_add', 'pre_remove'):
return
if reverse:
if model == Submission:
invalidate_content(Submission, instance)
seen_courses = set()
for submission_pk in pk_set:
submission = Submission.objects.get(pk=submission_pk)
course_instance = submission.exercise.course_instance
if course_instance.pk not in seen_courses:
CachedPoints.invalidate(course_instance, instance.user)
seen_courses.add(course_instance.pk)
