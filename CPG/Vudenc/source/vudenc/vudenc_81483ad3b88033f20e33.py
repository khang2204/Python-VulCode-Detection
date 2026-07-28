def test_every_extractedtext_qa(self):...
for et in ExtractedText.objects.all():
response = self.client.get(f'/qa/extractedtext/%s' % et.data_document_id,
    follow=True)
if response.status_code != 200:
print(et.data_document_id)
self.assertEqual(response.status_code, 200)
