def test_unidentifed_group_type(self):...
pk = self.objects.dg.pk
self.objects.doc.matched = True
self.objects.doc.save()
response = self.client.get(f'/datagroup/{pk}/')
self.assertIsInstance(response.context['extract_form'],
    ExtractionScriptForm, 'ExtractForm should be included in the page!')
self.objects.gt.code = 'UN'
self.objects.gt.save()
response = self.client.get(f'/datagroup/{pk}/')
self.assertFalse(response.context['extract_form'],
    'ExtractForm should not be included in the page!')
