@classmethod...
super(TestUpdateCasePriority, cls).setUpTestData()
cls.permission = 'testcases.change_testcase'
cls.case_update_url = reverse('ajax-update_cases_default_tester')
