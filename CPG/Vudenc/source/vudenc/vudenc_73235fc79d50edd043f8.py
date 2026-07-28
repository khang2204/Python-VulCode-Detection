def test_course_instance_submitters(self):...
students = self.current_course_instance.get_submitted_profiles()
self.assertEquals(1, len(students))
self.assertEquals('testUser', students[0].shortname)
submission2 = Submission.objects.create(exercise=self.base_exercise, grader
    =self.grader.userprofile)
submission2.submitters.add(self.user.userprofile)
students = self.current_course_instance.get_submitted_profiles()
self.assertEquals(1, len(students))
self.assertEquals('testUser', students[0].shortname)
submission3 = Submission.objects.create(exercise=self.base_exercise, grader
    =self.user.userprofile)
submission3.submitters.add(self.grader.userprofile)
students = self.current_course_instance.get_submitted_profiles()
self.assertEquals(2, len(students))
self.assertEquals('testUser', students[0].shortname)
self.assertEquals('grader', students[1].shortname)
