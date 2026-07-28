def test_course_instance_unicode_string(self):...
self.assertEquals('123456 test course: Fall 2011 day 1', str(self.
    current_course_instance))
self.assertEquals('123456 test course: Secret super course', str(self.
    hidden_course_instance))
