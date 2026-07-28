def test_product_card_location(self):...
response = self.client.get('/datadocument/179486/')
html = response.content.decode('utf-8')
e_idx = html.index('<h4>Extracted Text')
p_idx = html.index('<h4 class="d-inline">Products')
self.assertTrue(p_idx > e_idx,
    'Product card should come after Extracted Text card')
