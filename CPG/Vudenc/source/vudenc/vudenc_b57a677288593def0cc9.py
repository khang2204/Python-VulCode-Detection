@login_required()...
doc = get_object_or_404(DataDocument, pk=pk)
script = Script.objects.get(title='Manual (dummy)', script_type='EX')
extext, created = ExtractedText.objects.get_or_create(data_document=doc,
    extraction_script=script)
if created:
extext.doc_date = 'please add...'
ExtractedTextForm, HnPFormSet = create_detail_formset(doc)
ext_form = ExtractedTextForm(request.POST or None, instance=extext)
hp_formset = HnPFormSet(request.POST or None, instance=extext, prefix='habits')
if request.method == 'POST' and 'save' in request.POST:
if hp_formset.is_valid() and ext_form.is_valid():
context = {'doc': doc, 'ext_form': ext_form, 'hp_formset': hp_formset}
if not doc.extracted:
return render(request, template_name, context)
doc.extracted = True
hp_formset.save()
doc.save()
ext_form.save()
return HttpResponseRedirect(f'/habitsandpractices/{doc.pk}')
