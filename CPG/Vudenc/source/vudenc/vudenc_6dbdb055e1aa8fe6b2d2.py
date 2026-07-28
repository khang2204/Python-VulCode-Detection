def test_course_instance_visibility(self):...
self.assertTrue(self.current_course_instance.is_visible_to())
self.assertFalse(self.hidden_course_instance.is_visible_to())
self.assertTrue(self.current_course_instance.is_visible_to(self.user))
self.assertFalse(self.hidden_course_instance.is_visible_to(self.user))
self.assertTrue(self.current_course_instance.is_visible_to(self.superuser))
self.assertTrue(self.hidden_course_instance.is_visible_to(self.superuser))
