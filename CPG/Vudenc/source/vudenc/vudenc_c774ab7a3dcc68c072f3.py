def test_absent_extracted_text(self):...
for dd in DataDocument.objects.all():
ddid = dd.id
resp = self.client.get('/datadocument/%s/' % ddid)
self.assertEqual(resp.status_code, 200,
    'The page must return a 200 status code')
extracted_text = ExtractedText.objects.get(data_document=dd)
self.assertContains(resp, 'No Extracted Text exists for this Data Document')
self.assertContains(resp, '<h4>Extracted Text')
