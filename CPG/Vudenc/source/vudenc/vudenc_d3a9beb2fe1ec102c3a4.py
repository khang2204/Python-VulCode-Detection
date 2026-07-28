def test_bulk_create_post(self):...
"""docstring"""
doc = DataDocument.objects.create(data_group=self.objects.dg)
response = self.client.get(f'/datagroup/{self.objects.dg.pk}/')
self.assertEqual(response.context['bulk'], 1,
    'Not all DataDocuments linked to Product, bulk_create needed')
new_stub_id = Product.objects.all().aggregate(Max('id'))['id__max'] + 1
response = self.client.post(f'/datagroup/{self.objects.dg.pk}/', {'bulk': 1})
self.assertEqual(response.context['bulk'], 0,
    'Products linked to all DataDocuments, no bulk_create needed.')
product = ProductDocument.objects.get(document=doc).product
self.assertEqual(product.title, 'unknown',
    'Title should be unknown in bulk_create')
self.assertEqual(product.upc, f'stub_%s' % new_stub_id,
    'UPC should be created for second Product')
