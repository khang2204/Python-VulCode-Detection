def test_course_instance_open(self):...
self.assertFalse(self.past_course_instance.is_open())
self.assertTrue(self.current_course_instance.is_open())
self.assertFalse(self.future_course_instance.is_open())
