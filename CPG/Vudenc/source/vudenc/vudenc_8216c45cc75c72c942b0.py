def test_refuse_if_missing_no_case_run_pk(self):...
self.client.login(username=self.tester.username, password='password')
response = self.client.post(self.many_comments_url, {'comment':
    'new comment', 'run': []})
self.assertJSONEqual(str(response.content, encoding=settings.
    DEFAULT_CHARSET), {'rc': 1, 'response': 'No runs selected.'})
response = self.client.post(self.many_comments_url, {'comment': 'new comment'})
self.assertJSONEqual(str(response.content, encoding=settings.
    DEFAULT_CHARSET), {'rc': 1, 'response': 'No runs selected.'})
