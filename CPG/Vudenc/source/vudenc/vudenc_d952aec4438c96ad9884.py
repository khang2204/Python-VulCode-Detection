def test_num_forms(self):...
"""docstring"""
group_models = {'CO': ExtractedChemical, 'FU': ExtractedFunctionalUse, 'HP':
    ExtractedHabitsAndPractices, 'CP': ExtractedListPresence, 'HH':
    ExtractedHHRec}
for code, model in group_models.items():
if DataDocument.objects.filter(document_type__group_type__code=code,
doc = DataDocument.objects.filter(document_type__group_type__code=code,
    extractedtext__isnull=False).first()
response = self.client.get(reverse('data_document', kwargs={'pk': doc.pk}))
num_forms = response.context['detail_formset'].total_form_count()
children = model.objects.filter(extracted_text=doc.extractedtext).count()
if doc.detail_page_editable:
error = f'{model.__module__} should have one more forms than instances'
error = f'{model.__module__} should have the same number of forms as instances'
self.assertEqual(num_forms, children + 1, error)
self.assertEqual(num_forms, children, error)
