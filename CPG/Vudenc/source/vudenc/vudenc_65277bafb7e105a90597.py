def test_course_module_after_open(self):...
self.assertFalse(self.course_module.is_after_open(self.yesterday))
self.assertTrue(self.course_module.is_after_open(self.today))
self.assertTrue(self.course_module.is_after_open())
self.assertTrue(self.course_module.is_after_open(self.tomorrow))
self.assertTrue(self.course_module.is_after_open(self.two_days_from_now))
