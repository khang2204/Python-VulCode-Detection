def test_course_module_open(self):...
self.assertFalse(self.course_module.is_open(self.yesterday))
self.assertTrue(self.course_module.is_open(self.today))
self.assertTrue(self.course_module.is_open())
self.assertTrue(self.course_module.is_open(self.tomorrow))
self.assertFalse(self.course_module.is_open(self.two_days_from_now))
