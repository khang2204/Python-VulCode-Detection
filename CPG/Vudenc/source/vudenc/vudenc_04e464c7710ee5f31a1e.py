def test_product_facet_returns(self):...
response = self.c.get('/find/?q=insecticide')
brands = response.content.count(b'name="brand_name"')
self.assertTrue(brands > 10,
    'There should be ~143 product returns for this search term')
