def test_every_extractedtext(self):...
"""docstring"""
for et in ExtractedText.objects.all():
dd = et.data_document
ParentForm, ChildForm = create_detail_formset(dd, EXTRA)
extracted_text_form = ParentForm(instance=et)
child_formset = ChildForm(instance=et)
dd_child_model = get_extracted_models(dd.data_group.group_type.code)[1]
childform_model = child_formset.__dict__.get('queryset').__dict__.get('model')
self.assertEqual(dd_child_model, childform_model)
