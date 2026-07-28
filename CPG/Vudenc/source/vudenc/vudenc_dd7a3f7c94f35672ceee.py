def test_refuse_if_passed_case_run_pks_not_exist(self):...
self.client.login(username=self.tester.username, password='password')
response = self.client.post(self.many_comments_url, {'comment':
    'new comment', 'run': '99999998,1009900'})
self.assertJSONEqual(str(response.content, encoding=settings.
    DEFAULT_CHARSET), {'rc': 1, 'response': 'No caserun found.'})
