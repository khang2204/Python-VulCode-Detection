def test_data_document_qa(self):...
scr = Script.objects.annotate(num_ets=Count('extractedtext')).filter(
    num_ets__lt=100).filter(script_type='EX').first()
pk = ExtractedText.objects.filter(qa_group=None).filter(extraction_script=scr
    ).filter(data_document__data_group__group_type__code='CO').first().pk
response = self.client.get(f'/qa/extractedtext/{pk}/')
scr = ExtractedText.objects.get(pk=pk).extraction_script
group_count = QAGroup.objects.filter(extraction_script=scr).count()
self.assertTrue(group_count == 1)
self.assertTrue(scr.qa_begun)
new_group = QAGroup.objects.get(extraction_script=scr)
et = ExtractedText.objects.get(pk=pk)
self.assertTrue(et.qa_group == new_group)
response = self.client.get(f'/qa/extractionscript/')
self.assertIn(f"'/qa/extractionscript/{scr.pk}/'> Continue QA".encode(),
    response.content)
scr = Script.objects.annotate(num_ets=Count('extractedtext')).filter(
    num_ets__gt=100).first()
pk = ExtractedText.objects.filter(extraction_script=scr).first().pk
response = self.client.get(f'/qa/extractedtext/{pk}/')
scr = ExtractedText.objects.get(pk=pk).extraction_script
new_group = QAGroup.objects.get(extraction_script=scr)
initial_qa_count = ExtractedText.objects.filter(qa_group=new_group).count()
self.assertTrue(initial_qa_count > 100)
pk = ExtractedText.objects.filter(extraction_script_id=scr.id).filter(qa_group
    =None).first().pk
response = self.client.get(f'/qa/extractedtext/{pk}/')
self.assertGreater(ExtractedText.objects.filter(qa_group=new_group).count(),
    initial_qa_count)
