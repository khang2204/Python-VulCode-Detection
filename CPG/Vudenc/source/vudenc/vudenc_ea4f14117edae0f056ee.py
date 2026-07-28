def make_formset(parent_model, model, formset=BaseInlineFormSet, form=forms...
formset_fields = model.detail_fields()
if exclude:
formset_fields = [in_field for in_field in formset_fields if not in_field in
    exclude]
return forms.inlineformset_factory(parent_model=parent_model, model=model,
    fields=formset_fields, formset=formset, form=form, extra=extra,
    can_delete=can_delete)
