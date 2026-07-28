def test_qa_group_creation(self):...
pk = self.objects.extext.pk
self.assertIsNone(self.objects.extext.qa_group)
self.assertEqual(len(QAGroup.objects.all()), 0)
pk = self.objects.extext.extraction_script.pk
response = self.client.get(f'/qa/extractionscript/{pk}/')
self.assertEqual(response.status_code, 200)
qa_group = QAGroup.objects.get(extraction_script=self.objects.extext.
    extraction_script)
ext = ExtractedText.objects.get(qa_group=qa_group)
self.assertIsNotNone(ext.qa_group)
response = self.client.get(f'/qa/extractedtext/{ext.pk}/')
