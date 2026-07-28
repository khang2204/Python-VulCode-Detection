def test_update_plan_is_active(self):...
self.client.login(username=self.tester.username, password='password')
post_data = {'content_type': 'testplans.testplan', 'object_pk': self.plan.
    pk, 'field': 'is_active', 'value': 'False', 'value_type': 'bool'}
response = self.client.post(self.update_url, post_data)
self.assertJSONEqual(str(response.content, encoding=settings.
    DEFAULT_CHARSET), {'rc': 0, 'response': 'ok'})
plan = TestPlan.objects.get(pk=self.plan.pk)
self.assertFalse(plan.is_active)
