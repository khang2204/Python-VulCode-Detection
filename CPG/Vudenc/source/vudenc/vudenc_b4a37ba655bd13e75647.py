def test_detail_form_load(self):...
pk = self.objects.dg.pk
response = self.client.get(f'/datagroup/{pk}/')
self.assertFalse(self.objects.doc.matched,
    'Document should start w/ matched False')
self.assertFalse(self.objects.doc.extracted,
    'Document should start w/ extracted False')
self.assertFalse(response.context['datagroup'].all_matched(),
    'UploadForm should be included in the page!')
self.assertFalse(response.context['extract_form'],
    'ExtractForm should not be included in the page!')
self.objects.doc.matched = True
self.objects.doc.save()
response = self.client.get(f'/datagroup/{pk}/')
self.assertTrue(response.context['datagroup'].all_matched(),
    'UploadForm should not be included in the page!')
self.assertIsInstance(response.context['extract_form'],
    ExtractionScriptForm, 'ExtractForm should be included in the page!')
self.objects.doc.extracted = True
self.objects.doc.save()
response = self.client.get(f'/datagroup/{pk}/')
self.assertTrue(response.context['datagroup'].all_matched(),
    'UploadForm should not be included in the page!')
self.assertFalse(response.context['extract_form'],
    'ExtractForm should not be included in the page!')
