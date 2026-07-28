def create_detail_formset(document, extra=1, can_delete=False, exclude=[]):...
"""docstring"""
group_type = document.data_group.type
parent, child = get_extracted_models(group_type)
extracted = hasattr(document, 'extractedtext')
def make_formset(parent_model, model, formset=BaseInlineFormSet, form=forms...
formset_fields = model.detail_fields()
if exclude:
formset_fields = [in_field for in_field in formset_fields if not in_field in
    exclude]
return forms.inlineformset_factory(parent_model=parent_model, model=model,
    fields=formset_fields, formset=formset, form=form, extra=extra,
    can_delete=can_delete)
