def test_bulk_create_products_form(self):...
response = self.client.get(f'/datagroup/{self.objects.dg.pk}/')
self.assertEqual(response.context['bulk'], 0,
    'Product linked to all DataDocuments, no bulk_create needed.')
doc = DataDocument.objects.create(data_group=self.objects.dg)
doc.matched = True
self.objects.doc.matched = True
doc.save()
self.objects.doc.save()
response = self.client.get(f'/datagroup/{self.objects.dg.pk}/')
self.assertEqual(response.context['bulk'], 1,
    'Not all DataDocuments linked to Product, bulk_create needed')
self.assertIn('Bulk Create', response.content.decode(),
    'Bulk create button should be present.')
p = Product.objects.create(upc='stub_47', data_source=self.objects.ds)
ProductDocument.objects.create(document=doc, product=p)
response = self.client.get(f'/datagroup/{self.objects.dg.pk}/')
self.assertEqual(response.context['bulk'], 0,
    'Product linked to all DataDocuments, no bulk_create needed.')
self.objects.dg.group_type = GroupType.objects.create(title=
    'Habits and practices')
response = self.client.get(f'/datagroup/{self.objects.dg.pk}/')
self.assertNotIn('Bulk Create', response.content.decode(),
    "Bulk button shouldn't be present w/ Habits and practices group_type.")
