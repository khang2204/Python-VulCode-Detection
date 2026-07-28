def test_faceted_search_excludes_chemicals(self):...
response = self.c.get('/find/?q=ethyl')
self.assertContains(response, 'Data Document')
self.assertNotContains(response, 'Extracted Chemical')
self.assertNotContains(response, 'DSSTox Substance')
