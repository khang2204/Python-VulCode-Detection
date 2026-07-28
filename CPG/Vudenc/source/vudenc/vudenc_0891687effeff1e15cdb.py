def test_script_links(self):...
doc = DataDocument.objects.first()
response = self.client.get(f'/datadocument/179486/')
self.assertIn('Download Script', response.content.decode('utf-8'))
self.assertIn('Extraction Script', response.content.decode('utf-8'))
