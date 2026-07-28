def test_product_create_link(self):...
response = self.client.get('/datadocument/167497/')
self.assertContains(response, '/link_product_form/167497/')
data = {'title': ['New Product'], 'upc': ['stub_1860'], 'document_type': [1
    ], 'return_url': ['/datadocument/167497/']}
response = self.client.post('/link_product_form/167497/', data=data)
self.assertRedirects(response, '/datadocument/167497/')
response = self.client.get(response.url)
self.assertContains(response, 'New Product')
