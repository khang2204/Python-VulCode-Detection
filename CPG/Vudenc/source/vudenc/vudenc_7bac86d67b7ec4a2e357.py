def test_qa_approval_redirect(self):...
self.client.get(f'/qa/extractionscript/{self.objects.exscript.pk}/')
pk = self.objects.extext.pk
response = self.client.post(f'/qa/extractedtext/{pk}/', {'approve': [47]})
self.assertEqual(response.url, '/qa/extractionscript/',
    'User should be redirected to QA homepage after last extext is approved.')
