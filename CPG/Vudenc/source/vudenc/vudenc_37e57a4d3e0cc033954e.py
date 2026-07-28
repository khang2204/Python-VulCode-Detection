def test_upload_note(self):...
response = self.client.get(f'/datagroup/{DataGroup.objects.first().id}/'
    ).content.decode('utf8')
self.assertIn('Please limit upload to <600 documents at one time', response,
    'Note to limit upload to <600 should be on the page')
