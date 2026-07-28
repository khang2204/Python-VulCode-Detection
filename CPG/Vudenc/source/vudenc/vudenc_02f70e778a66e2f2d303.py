def test_cpcat_qa(self):...
response = self.client.get(f'/qa/chemicalpresence/')
self.assertIn(f"/qa/chemicalpresencegroup/49/'> View Chemical Presence Lists"
    .encode(), response.content)
response = self.client.get(f'/qa/chemicalpresencegroup/49', follow=True)
self.assertIn(f'/qa/extractedtext/254781/"> Begin QA'.encode(), response.
    content)
elps = ExtractedListPresence.objects.filter(extracted_text__data_document_id
    =254781)
self.assertEqual(elps.filter(qa_flag=True).count(), 0)
response = self.client.get(f'/qa/extractedtext/254781/', follow=True)
elps = ExtractedListPresence.objects.filter(extracted_text__data_document_id
    =254781)
self.assertEqual(elps.filter(qa_flag=True).count(), 30)
elp_flagged = elps.filter(qa_flag=True).first()
self.assertIn(elp_flagged.raw_cas.encode(), response.content)
elp_not_flagged = elps.filter(qa_flag=False).first()
self.assertNotIn(elp_not_flagged.raw_cas.encode(), response.content)
