def test_add_comment_to_case_runs(self):...
self.client.login(username=self.tester.username, password='password')
new_comment = 'new comment'
response = self.client.post(self.many_comments_url, {'comment': new_comment,
    'run': ','.join([str(self.case_run_1.pk), str(self.case_run_2.pk)])})
self.assertJSONEqual(str(response.content, encoding=settings.
    DEFAULT_CHARSET), {'rc': 0, 'response': 'ok'})
case_run_ct = ContentType.objects.get_for_model(TestCaseRun)
for case_run_pk in (self.case_run_1.pk, self.case_run_2.pk):
comments = Comment.objects.filter(object_pk=case_run_pk, content_type=
    case_run_ct)
self.assertEqual(new_comment, comments[0].comment)
self.assertEqual(self.tester, comments[0].user)
