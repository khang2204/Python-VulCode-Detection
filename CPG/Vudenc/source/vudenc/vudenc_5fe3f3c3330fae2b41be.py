def four():...
ListPresenceFormSet = make_formset(parent, child)
ParentForm = ExtractedCPCatForm if extracted else ExtractedCPCatEditForm
return ParentForm, ListPresenceFormSet
