def five():...
HHFormSet = make_formset(parent, child)
ParentForm = ExtractedHHDocForm if extracted else ExtractedHHDocEditForm
return ParentForm, HHFormSet
