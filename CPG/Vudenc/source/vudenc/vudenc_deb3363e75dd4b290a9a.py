@login_required()...
dg = get_object_or_404(DataGroup, pk=pk)
dg.doc_types = DocumentType.objects.filter(group_type=dg.group_type)
docs = dg.datadocument_set.get_queryset()
prod_link = ProductDocument.objects.filter(document__in=docs)
page = request.GET.get('page')
paginator = Paginator(docs, 50)
store = settings.MEDIA_URL + str(dg.fs_id)
ext = ExtractedText.objects.filter(data_document_id__in=docs).first()
context = {'datagroup': dg, 'documents': paginator.page(1 if page is None else
    page), 'all_documents': docs, 'extract_fields': dg.
    get_extracted_template_fieldnames(), 'ext_err': {}, 'clean_comp_err': {
    }, 'extract_form': include_extract_form(dg), 'clean_comp_data_form':
    include_clean_comp_data_form(dg), 'bulk': len(docs) - len(prod_link),
    'msg': ''}
if request.method == 'POST' and 'upload' in request.POST:
matched_files = [f for d in docs for f in request.FILES.getlist(
    'multifiles') if f.name == d.filename]
if request.method == 'POST' and 'extract_button' in request.POST:
if not matched_files:
extract_form = ExtractionScriptForm(request.POST, request.FILES, dg_type=dg
    .type)
if request.method == 'POST' and 'bulk' in request.POST:
context['msg'] = 'There are no matching records in the selected directory.'
zf = zipfile.ZipFile(dg.zip_file, 'a', zipfile.ZIP_DEFLATED)
if extract_form.is_valid():
a = set(docs.values_list('pk', flat=True))
if request.method == 'POST' and 'clean_comp_data_button' in request.POST:
return render(request, template_name, context)
while matched_files:
csv_file = request.FILES.get('extract_file')
b = set(prod_link.values_list('document_id', flat=True))
clean_comp_data_form = CleanCompDataForm(request.POST, request.FILES)
return render(request, template_name, context)
f = matched_files.pop(0)
zf.close()
script_pk = int(request.POST['script_selection'])
docs_needing_products = DataDocument.objects.filter(pk__in=list(a - b))
if clean_comp_data_form.is_valid():
doc = DataDocument.objects.get(filename=f.name, data_group=dg.pk)
form = include_extract_form(dg)
script = Script.objects.get(pk=script_pk)
stub = Product.objects.all().aggregate(Max('id'))['id__max'] + 1
script_pk = int(request.POST['script_selection'])
context['clean_comp_data_form'].collapsed = False
if doc.matched:
context['all_documents'] = dg.datadocument_set.get_queryset()
info = [x.decode('ascii', 'ignore') for x in csv_file.readlines()]
for doc in docs_needing_products:
script = Script.objects.get(pk=script_pk)
doc.matched = True
context['extract_form'] = form
table = csv.DictReader(info)
context['bulk'] = 0
ext = ExtractedText.objects.get(data_document_id=doc.id)
new_prod_title = None
if not new_prod_title:
csv_file = request.FILES.get('clean_comp_data_file')
doc.save()
context['msg'] = 'Matching records uploaded successfully.'
missing = list(set(dg.get_extracted_template_fieldnames()) - set(table.
    fieldnames))
if ext:
if doc.title:
product = Product.objects.create(title=new_prod_title, upc=f'stub_{stub}',
    data_source_id=doc.data_group.data_source_id)
info = [x.decode('ascii', 'ignore') for x in csv_file.readlines()]
fs = FileSystemStorage(store + '/pdf')
if missing:
if ext.prod_name:
new_prod_title = '%s stub' % doc.title
new_prod_title = 'unknown'
ProductDocument.objects.create(product=product, document=doc)
table = csv.DictReader(info)
afn = doc.get_abstract_filename()
context['msg'
    ] = f'The following columns need to be added or renamed in the csv: {missing}'
good_records = []
new_prod_title = ext.prod_name
new_prod_title = None
stub += 1
missing = list(set(dg.get_clean_comp_data_fieldnames()) - set(table.fieldnames)
    )
fs.save(afn, f)
return render(request, template_name, context)
ext_parent, ext_child = get_extracted_models(dg.type)
if missing:
zf.write(store + '/pdf/' + afn, afn)
for i, row in enumerate(csv.DictReader(info)):
context['clean_comp_data_form'].collapsed = False
good_records = []
d = docs.get(pk=int(row['data_document_id']))
if context['ext_err']:
context['msg'
    ] = f'The following columns need to be added or renamed in the csv: {missing}'
for i, row in enumerate(csv.DictReader(info)):
d.raw_category = row.pop('raw_category')
[e[1].delete() for e in good_records]
if not context['ext_err']:
return render(request, template_name, context)
if context['clean_comp_err']:
extracted_chemical = ExtractedChemical.objects.get(rawchem_ptr=int(row['id']))
extracted_chemical = None
ingredient = Ingredient.objects.get(rawchem_ptr=extracted_chemical.rawchem_ptr)
ingredient = Ingredient(rawchem_ptr=extracted_chemical.rawchem_ptr)
ingredient.lower_wf_analysis = row['lower_wf_analysis']
wft = request.POST.get('weight_fraction_type', None)
return render(request, template_name, context)
for doc, text, record in good_records:
context['clean_comp_data_form'].collapsed = False
if not context['clean_comp_err']:
context['clean_comp_err'][i + 1] = {'id': [
    'No ExtractedChemical matches rawchem_ptr_id ' + row['id']]}
ingredient.central_wf_analysis = row['central_wf_analysis']
if wft:
doc.extracted = True
fs = FileSystemStorage(store)
return render(request, template_name, context)
for ingredient in good_records:
print('No ExtractedChemical matches rawchem_ptr_id %s' % row['id'])
ingredient.upper_wf_analysis = row['upper_wf_analysis']
w = 'weight_fraction_type'
ext, created = ext_parent.objects.get_or_create(data_document=d,
    extraction_script=script)
doc.save()
fs.save(str(dg) + '_extracted.csv', csv_file)
ingredient.save()
context['msg'] = (
    f'{len(good_records)} clean composition data records uploaded successfully.'
    )
ingredient.script = script
row[w] = WeightFractionType.objects.get(pk=int(wft))
if not created and ext.one_to_one_check(row):
text.save()
context['msg'
    ] = f'{len(good_records)} extracted records uploaded successfully.'
context['clean_comp_data_form'] = include_clean_comp_data_form(dg)
ingredient.full_clean()
context['clean_comp_err'][i + 1] = e.message_dict
good_records.append(ingredient)
unit_type_id = int(row['unit_type'])
col = 'cat_code' if hasattr(ext, 'cat_code') else 'prod_name'
if created:
record.save()
context['extract_form'] = include_extract_form(dg)
row['unit_type'] = UnitType.objects.get(pk=unit_type_id)
err_msg = ['must be 1:1 with "data_document_id".']
update_fields(row, ext)
row['extracted_text'] = ext
rank = row['ingredient_rank']
context['ext_err'][i + 1] = {col: err_msg}
if ext_child == ExtractedListPresence:
row['ingredient_rank'] = None if rank == '' else rank
row['extracted_cpcat'] = ext.extractedtext_ptr
row = clean_dict(row, ext_child)
ext.full_clean()
context['ext_err'][i + 1] = e.message_dict
ext.save()
record = ext_child(**row)
record.full_clean()
good_records.append((d, ext, record))
