def one():...
ChemicalFormSet = make_formset(parent_model=parent, model=child, formset=
    ExtractedChemicalFormSet, form=ExtractedChemicalForm)
return ExtractedTextForm, ChemicalFormSet
