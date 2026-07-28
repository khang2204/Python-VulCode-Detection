def test_detail_datasource_link(self):...
pk = self.objects.dg.pk
response = self.client.get(f'/datagroup/{pk}/')
self.assertContains(response, '<a href="/datasource/', msg_prefix=
    'Should be able to get back to DataSource from here.')
