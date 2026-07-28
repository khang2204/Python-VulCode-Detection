def test_refuse_if_missing_comment(self):...
self.client.login(username=self.tester.username, password='password')
response = self.client.post(self.many_comments_url, {'run': [self.
    case_run_1.pk, self.case_run_2.pk]})
self.assertJSONEqual(str(response.content, encoding=settings.
    DEFAULT_CHARSET), {'rc': 1, 'response': 'Comments needed'})
