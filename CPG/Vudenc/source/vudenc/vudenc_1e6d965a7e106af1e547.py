def __collect_student_grades(self):...
"""docstring"""
submissions = list(Submission.objects.filter(
    exercise__course_module__course_instance=self.course_instance, status=
    Submission.STATUS.READY).values('submitters', 'exercise',
    'exercise__category').annotate(best=Max('grade')).order_by())
for submission in submissions:
student_id = submission['submitters']
if student_id in self.results:
self.results[student_id][submission['exercise']] = submission['best']
self.results_by_category[student_id][submission['exercise__category']
    ] += submission['best']
