def test_hidden_fields(self):...
"""docstring"""
response = self.client.get('/qa/extractionscript/15/', follow=True)
response = self.client.get('/qa/extractedtext/5/', follow=True)
self.assertIn(b'<input type="text" name="rawchem-1-raw_cas"', response.content)
self.assertNotIn(b'<input type="text" name="rawchem-1-unit_type"', response
    .content)
self.assertIn(b'Functional Use Chem1', response.content)
response = self.client.get('/qa/extractionscript/5', follow=True)
response = self.client.get('/qa/extractedtext/7/', follow=True)
self.assertIn(b'rawchem-1-unit_type', response.content)
