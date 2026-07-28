def test_refuse_if_missing_permission(self):...
self.client.login(username=self.tester.username, password='password')
remove_perm_from_user(self.tester, self.permission)
post_data = {'content_type': 'testplans.testplan', 'object_pk': self.plan.
    pk, 'field': 'is_active', 'value': 'False', 'value_type': 'bool'}
response = self.client.post(self.update_url, post_data)
self.assertJSONEqual(str(response.content, encoding=settings.
    DEFAULT_CHARSET), {'rc': 1, 'response': 'Permission Dinied.'})
