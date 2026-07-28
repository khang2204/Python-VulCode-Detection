def test_product_title_duplication(self):...
response = self.client.get('/datadocument/245401/')
self.assertContains(response, '/link_product_form/245401/')
data = {'title': ['Product Title'], 'upc': ['stub_9100'], 'document_type':
    [1], 'return_url': ['/datadocument/245401/']}
response = self.client.post('/link_product_form/245401/', data=data)
self.assertRedirects(response, '/datadocument/245401/')
response = self.client.get(response.url)
new_product = Product.objects.get(upc='stub_9100')
self.assertContains(response, f'product/%s' % new_product.id)
data = {'title': ['Product Title'], 'upc': ['stub_9101'], 'document_type':
    [1], 'return_url': ['/datadocument/245401/']}
response = self.client.post('/link_product_form/245401/', data=data)
self.assertRedirects(response, '/datadocument/245401/')
response = self.client.get(response.url)
new_product = Product.objects.get(upc='stub_9101')
self.assertContains(response, f'product/%s' % new_product.id)
