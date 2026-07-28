def get(self, request, *args, **kwargs):...
exercisecollection = None
exercisecollection_title = None
submission_allowed = False
disable_submit = False
should_enroll = False
issues = []
students = [self.profile]
if self.exercise.is_submittable:
SUBMIT_STATUS = self.exercise.SUBMIT_STATUS
if self.exercise.status == LearningObject.STATUS.MAINTENANCE or self.module.status == CourseModule.STATUS.MAINTENANCE:
submission_status, submission_allowed, issues, students = (self.
    submission_check())
if self.is_course_staff:
if hasattr(self.exercise, 'generate_table_of_contents'
self.get_summary_submissions()
issue = _('Exercise is in maintenance and content is hidden from students.')
page = ExercisePage(self.exercise)
self.toc = self.content.children_hierarchy(self.exercise)
page = self.exercise.as_leaf_class().load(request, students, url_name=self.
    post_url_name)
disable_submit = submission_status in [SUBMIT_STATUS.CANNOT_ENROLL,
    SUBMIT_STATUS.NOT_ENROLLED]
messages.error(request, issue)
page.content = _('Unfortunately this exercise is currently under maintenance.')
self.note('toc')
if self.profile:
should_enroll = submission_status == SUBMIT_STATUS.NOT_ENROLLED
issues.append(issue)
return super().get(request, *args, page=page, students=students, **kwargs)
LearningObjectDisplay.objects.create(learning_object=self.exercise, profile
    =self.profile)
if isinstance(self.exercise, ExerciseCollection):
exercisecollection, exercisecollection_title = self.__load_exercisecollection(
    request)
return super().get(request, *args, page=page, students=students,
    submission_allowed=submission_allowed, disable_submit=disable_submit,
    should_enroll=should_enroll, issues=issues, exercisecollection=
    exercisecollection, exercisecollection_title=exercisecollection_title,
    **kwargs)
