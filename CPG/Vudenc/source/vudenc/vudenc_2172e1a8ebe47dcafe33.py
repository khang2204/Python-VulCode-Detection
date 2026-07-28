def test_extracted_count(self):...
response = self.client.get(f'/datagroup/{DataGroup.objects.first().id}/'
    ).content.decode('utf8')
self.assertIn('0 extracted', response,
    'Data Group should contain a count of 0 total extracted documents')
self.objects.doc.extracted = True
self.objects.doc.save()
response = self.client.get(f'/datagroup/{DataGroup.objects.first().id}/'
    ).content.decode('utf8')
self.assertIn('1 extracted', response,
    'Data Group should contain a count of 1 total extracted documents')
