def test_refuse_if_missing_permission(self):...
remove_perm_from_user(self.tester, self.permission)
self.client.login(username=self.tester.username, password='password')
response = self.client.post(self.case_update_url, {'target_field':
    'priority', 'from_plan': self.plan.pk, 'case': [self.case_1.pk, self.
    case_3.pk], 'new_value': Priority.objects.get(value='P3').pk})
self.assertJSONEqual(str(response.content, encoding=settings.
    DEFAULT_CHARSET), {'rc': 1, 'response':
    "You don't have enough permission to update TestCases."})
