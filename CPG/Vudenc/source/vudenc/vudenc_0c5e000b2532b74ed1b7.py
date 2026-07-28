def test_new_qa_group_urls(self):...
response = self.client.get(f'/qa/extractionscript/')
self.assertIn(f"/qa/extractionscript/15/'> Begin QA".encode(), response.content
    )
pk = 15
response = self.client.get(f'/qa/extractionscript/{pk}/')
et = ExtractedText.objects.filter(extraction_script=pk).first()
self.assertIn(f'/qa/extractedtext/{et.pk}/'.encode(), response.content)
group_count = QAGroup.objects.filter(extraction_script_id=pk).count()
self.assertTrue(group_count == 1)
self.assertTrue(Script.objects.get(pk=15).qa_begun)
group_pk = QAGroup.objects.get(extraction_script_id=pk).pk
et = ExtractedText.objects.filter(extraction_script=pk).first()
self.assertTrue(et.qa_group_id == group_pk)
response = self.client.get(f'/qa/extractionscript/')
self.assertIn(f"'/qa/extractionscript/15/'> Continue QA".encode(), response
    .content)
