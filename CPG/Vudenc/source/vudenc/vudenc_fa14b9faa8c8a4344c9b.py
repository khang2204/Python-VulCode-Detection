def test_curated_chemical(self):...
"""docstring"""
for et in ExtractedText.objects.all():
dd = et.data_document
ParentForm, ChildForm = create_detail_formset(dd)
child_formset = ChildForm(instance=et)
for form in child_formset.forms:
if dd.data_group.type in ['CO', 'UN']:
ec = form.instance
self.assertFalse('true_cas' in form.fields)
if ec.dsstox is not None:
self.assertTrue('true_cas' in form.fields)
self.assertFalse('true_cas' in form.fields)
self.assertTrue('SID' in form.fields)
self.assertFalse('SID' in form.fields)
