def test_update_case_priority(self):...
self.client.login(username=self.tester.username, password='password')
response = self.client.post(self.case_update_url, {'target_field':
    'priority', 'from_plan': self.plan.pk, 'case': [self.case_1.pk, self.
    case_3.pk], 'new_value': Priority.objects.get(value='P3').pk})
self.assertJSONEqual(str(response.content, encoding=settings.
    DEFAULT_CHARSET), {'rc': 0, 'response': 'ok'})
for pk in (self.case_1.pk, self.case_3.pk):
self.assertEqual('P3', TestCase.objects.get(pk=pk).priority.value)
