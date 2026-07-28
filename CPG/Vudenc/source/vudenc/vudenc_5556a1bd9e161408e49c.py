def test_course_url(self):...
self.assertEqual('/Course-Url/T-00.1000_d1/', self.current_course_instance.
    get_absolute_url())
self.assertEqual('/Course-Url/T-00.1000_hidden/', self.
    hidden_course_instance.get_absolute_url())
