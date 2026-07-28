def test_groups(self):...
group = StudentGroup(course_instance=self.current_course_instance)
group.save()
group.members.add(self.user.userprofile, self.grader.userprofile)
self.assertEqual(StudentGroup.get_exact(self.current_course_instance, [self
    .user.userprofile, self.grader.userprofile]), group)
self.assertEqual(StudentGroup.get_exact(self.current_course_instance, [self
    .user.userprofile, self.superuser.userprofile]), None)
