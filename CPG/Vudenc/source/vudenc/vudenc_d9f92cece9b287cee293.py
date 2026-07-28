def test_detail_table_headers(self):...
pk = self.objects.dg.pk
response = self.client.get(f'/datagroup/{pk}/').content.decode('utf8')
self.assertIn('<th>Product</th>', response,
    'Data Group should have Product column.')
fu = GroupType.objects.create(title='Functional use')
self.objects.dg.group_type = fu
self.objects.dg.save()
response = self.client.get(f'/datagroup/{pk}/').content.decode('utf8')
self.assertNotIn('<th>Product</th>', response,
    'Data Group should have Product column.')
