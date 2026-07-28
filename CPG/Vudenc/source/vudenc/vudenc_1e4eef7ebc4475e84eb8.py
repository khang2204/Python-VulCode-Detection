def test_fetch_extracted_records(self):...
"""docstring"""
for et in ExtractedText.objects.all():
for ex_child in et.fetch_extracted_records():
child_model = ex_child.__class__
self.assertEqual(et.pk, child_model.objects.get(pk=ex_child.pk).
    extracted_text.pk,
    'The ExtractedChemical object with the returned child pk should have the correct extracted_text parent'
    )
