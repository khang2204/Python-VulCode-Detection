def test_faceted_search_renders_div(self):...
response = self.c.get('/find/?q=terro')
self.assertNotContains(response, '<table')
self.assertContains(response, '<div class="results-wrapper">')
