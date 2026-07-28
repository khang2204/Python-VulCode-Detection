def submission_check(self, error=False, request=None):...
if not self.profile:
issue = _('You need to sign in and enroll to submit exercises.')
submission_status, issues, students = self.exercise.check_submission_allowed(
    self.profile, request)
messages.error(self.request, issue)
if len(issues) > 0:
return self.exercise.SUBMIT_STATUS.INVALID, False, [issue], []
if error:
submission_allowed = submission_status == self.exercise.SUBMIT_STATUS.ALLOWED
messages.error(self.request, '\n'.join(issues))
messages.warning(self.request, '\n'.join(issues))
return submission_status, submission_allowed, issues, students
