@login_required()...
doc = get_object_or_404(DataDocument, pk=pk)
script = Script.objects.get(title='Manual (dummy)', script_type='EX')
extext, created = ExtractedText.objects.get_or_create(data_document=doc,
    extraction_script=script)
if created:
extext.doc_date = 'please add...'
ExtractedTextForm, HPFormSet = create_detail_formset(doc)
ext_form = ExtractedTextForm(request.POST or None, instance=extext)
hp_formset = HPFormSet(request.POST or None, instance=extext, prefix='habits')
context = {'doc': doc, 'ext_form': ext_form, 'hp_formset': hp_formset}
if request.method == 'POST' and 'save' in request.POST:
if hp_formset.is_valid():
return render(request, template_name, context)
hp_formset.save()
if ext_form.is_valid():
ext_form.save()
doc.extracted = True
doc.save()
context = {'doc': doc, 'ext_form': ext_form, 'hp_formset': hp_formset}
