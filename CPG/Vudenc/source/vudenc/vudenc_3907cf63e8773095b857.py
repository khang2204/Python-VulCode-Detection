@classmethod...
super(TestUpdateCaseRunStatus, cls).setUpTestData()
cls.permission = 'testruns.change_testcaserun'
cls.update_url = reverse('ajax-update_case_run_status')
