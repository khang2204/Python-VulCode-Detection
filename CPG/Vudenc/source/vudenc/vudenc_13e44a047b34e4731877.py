def test_course_staff(self):...
self.assertFalse(self.course.is_teacher(self.user))
self.assertFalse(self.current_course_instance.is_assistant(self.user))
self.assertFalse(self.current_course_instance.is_teacher(self.user))
self.assertFalse(self.current_course_instance.is_course_staff(self.user))
self.assertEquals(0, len(self.current_course_instance.
    get_course_staff_profiles()))
self.current_course_instance.assistants.add(self.user.userprofile)
self.assertFalse(self.course.is_teacher(self.user))
self.assertTrue(self.current_course_instance.is_assistant(self.user))
self.assertFalse(self.current_course_instance.is_teacher(self.user))
self.assertTrue(self.current_course_instance.is_course_staff(self.user))
self.assertEquals(1, len(self.current_course_instance.
    get_course_staff_profiles()))
self.course.teachers.add(self.user.userprofile)
self.assertTrue(self.course.is_teacher(self.user))
self.assertTrue(self.current_course_instance.is_assistant(self.user))
self.assertTrue(self.current_course_instance.is_teacher(self.user))
self.assertTrue(self.current_course_instance.is_course_staff(self.user))
self.assertEquals(1, len(self.current_course_instance.
    get_course_staff_profiles()))
self.assertEquals('testUser', self.current_course_instance.
    get_course_staff_profiles()[0].shortname)
self.current_course_instance.assistants.clear()
self.assertTrue(self.course.is_teacher(self.user))
self.assertFalse(self.current_course_instance.is_assistant(self.user))
self.assertTrue(self.current_course_instance.is_teacher(self.user))
self.assertTrue(self.current_course_instance.is_course_staff(self.user))
self.assertEquals(1, len(self.current_course_instance.
    get_course_staff_profiles()))
self.course.teachers.clear()
self.assertFalse(self.course.is_teacher(self.user))
self.assertFalse(self.current_course_instance.is_assistant(self.user))
self.assertFalse(self.current_course_instance.is_teacher(self.user))
self.assertFalse(self.current_course_instance.is_course_staff(self.user))
self.assertEquals(0, len(self.current_course_instance.
    get_course_staff_profiles()))
