def post(self, request, *args, **kwargs):...
if not self.exercise.is_submittable:
return self.http_method_not_allowed(request, *args, **kwargs)
new_submission = None
page = ExercisePage(self.exercise)
submission_status, submission_allowed, issues, students = (self.
    submission_check(True, request))
if submission_allowed:
new_submission = Submission.objects.create_from_post(self.exercise,
    students, request)
self.get_summary_submissions()
if new_submission:
return self.response(page=page, students=students, submission=new_submission)
page = self.exercise.grade(request, new_submission, url_name=self.post_url_name
    )
messages.error(request, _(
    'The submission could not be saved for some reason. The submission was not registered.'
    ))
if self.exercise.status in (LearningObject.STATUS.ENROLLMENT,
if not request.is_ajax() and '__r' in request.GET:
self.instance.enroll_student(self.request.user)
if not request.is_ajax() and '__r' not in request.GET:
return self.redirect(request.GET['__r'], backup=self.exercise)
return self.redirect(new_submission.get_absolute_url() + ('?wait=1' if page
    .is_wait else ''))
