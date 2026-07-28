def test_course_module_late_submission_point_worth(self):...
self.assertEquals(0, self.course_module.get_late_submission_point_worth())
self.assertEquals(80, self.course_module_with_late_submissions_allowed.
    get_late_submission_point_worth())
