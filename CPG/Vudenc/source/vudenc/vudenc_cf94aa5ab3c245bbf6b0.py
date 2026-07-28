def setUp(self):...
self.client = Client()
self.user = User(username='testUser')
self.user.set_password('testPassword')
self.user.save()
self.grader = User(username='grader', is_staff=True)
self.grader.set_password('graderPassword')
self.grader.save()
self.superuser = User(username='staff', is_staff=False, is_superuser=True)
self.superuser.set_password('staffPassword')
self.superuser.save()
self.course = Course.objects.create(name='test course', code='123456', url=
    'Course-Url')
self.today = timezone.now()
self.tomorrow = self.today + timedelta(days=1)
self.two_days_from_now = self.tomorrow + timedelta(days=1)
self.yesterday = self.today - timedelta(days=1)
self.past_course_instance = CourseInstance.objects.create(instance_name=
    'Fall 2011 day 0', starting_time=self.yesterday, ending_time=self.today,
    course=self.course, url='T-00.1000_d0')
self.current_course_instance = CourseInstance.objects.create(instance_name=
    'Fall 2011 day 1', starting_time=self.today, ending_time=self.tomorrow,
    course=self.course, url='T-00.1000_d1')
self.future_course_instance = CourseInstance.objects.create(instance_name=
    'Fall 2011 day 2', starting_time=self.tomorrow, ending_time=self.
    two_days_from_now, course=self.course, url='T-00.1000_d2')
self.hidden_course_instance = CourseInstance.objects.create(instance_name=
    'Secret super course', starting_time=self.tomorrow, ending_time=self.
    two_days_from_now, course=self.course, url='T-00.1000_hidden',
    visible_to_students=False)
self.course_module = CourseModule.objects.create(name='test module', url=
    'test-module', points_to_pass=10, course_instance=self.
    current_course_instance, opening_time=self.today, closing_time=self.
    tomorrow)
self.course_module_with_late_submissions_allowed = CourseModule.objects.create(
    name='test module', url='test-module-late', points_to_pass=50,
    course_instance=self.current_course_instance, opening_time=self.today,
    closing_time=self.tomorrow, late_submissions_allowed=True,
    late_submission_deadline=self.two_days_from_now,
    late_submission_penalty=0.2)
self.learning_object_category = LearningObjectCategory.objects.create(name=
    'test category', course_instance=self.current_course_instance,
    points_to_pass=5)
self.learning_object = LearningObject.objects.create(name=
    'test learning object', course_module=self.course_module, category=self
    .learning_object_category, url='l1')
self.broken_learning_object = LearningObject.objects.create(name=
    'test learning object', course_module=self.
    course_module_with_late_submissions_allowed, category=self.
    learning_object_category, url='l2')
self.base_exercise = BaseExercise.objects.create(name='test exercise',
    course_module=self.course_module, category=self.
    learning_object_category, service_url='http://localhost/', url='b1')
self.submission = Submission.objects.create(exercise=self.base_exercise,
    grader=self.grader.userprofile)
self.submission.submitters.add(self.user.userprofile)
self.course_hook = CourseHook.objects.create(hook_url='test_hook_url',
    course_instance=self.current_course_instance)
