def test_change_case_run_status(self):...
self.client.login(username=self.tester.username, password='password')
response = self.client.post(self.update_url, {'content_type':
    'testruns.testcaserun', 'object_pk': self.case_run_1.pk, 'field':
    'case_run_status', 'value': str(TestCaseRunStatus.objects.get(name=
    'PAUSED').pk), 'value_type': 'int'})
self.assertJSONEqual(str(response.content, encoding=settings.
    DEFAULT_CHARSET), {'rc': 0, 'response': 'ok'})
self.assertEqual('PAUSED', TestCaseRun.objects.get(pk=self.case_run_1.pk).
    case_run_status.name)
