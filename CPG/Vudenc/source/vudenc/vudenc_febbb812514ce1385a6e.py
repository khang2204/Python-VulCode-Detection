@login_required()...
datasource = get_object_or_404(DataSource, pk=pk)
group_key = DataGroup.objects.filter(data_source=datasource).count() + 1
default_name = '{} {}'.format(datasource.title, group_key)
header = 'Create New Data Group For Data Source "' + str(datasource) + '"'
initial_values = {'downloaded_by': request.user, 'name': default_name,
    'data_source': datasource}
if request.method == 'POST':
form = DataGroupForm(request.POST, request.FILES, user=request.user,
    initial=initial_values)
groups = GroupType.objects.all()
if form.is_valid():
for group in groups:
datagroup = form.save()
context = {'form': form, 'header': header, 'datasource': datasource,
    'groups': groups}
group.codes = DocumentType.objects.filter(group_type=group)
form = DataGroupForm(user=request.user, initial=initial_values)
info = [x.decode('ascii', 'ignore') for x in datagroup.csv.readlines()]
return render(request, template_name, context)
table = csv.DictReader(info)
good_fields = ['filename', 'title', 'document_type', 'url', 'organization']
if not table.fieldnames == good_fields:
datagroup.csv.close()
text = ['DataDocument_id,' + ','.join(table.fieldnames) + '\n']
datagroup.delete()
errors = []
return render(request, template_name, {'field_error': table.fieldnames,
    'good_fields': good_fields, 'form': form})
filenames = []
count = 0
for line in table:
count += 1
if errors:
doc_type = DocumentType.objects.get(pk=1)
datagroup.csv.close()
datagroup.save()
code = line['document_type']
datagroup.delete()
myfile = File(f)
if line['filename'] == '':
return render(request, template_name, {'line_errors': errors, 'form': form})
myfile.write(''.join(text))
errors.append([count, "Filename can't be empty!"])
if len(line['filename']) > 255:
new_zip_name = Path(settings.MEDIA_URL + '/' + str(datagroup.fs_id) + '/' +
    str(datagroup.fs_id) + '.zip')
errors.append([count, 'Filename too long!'])
if line['filename'] in filenames:
new_zip_path = Path(settings.MEDIA_ROOT + '/' + str(datagroup.fs_id) + '/' +
    str(datagroup.fs_id) + '.zip')
errors.append([count, 'Duplicate filename found in csv'])
if line['title'] == '':
zf = zipfile.ZipFile(str(new_zip_path), 'w', zipfile.ZIP_DEFLATED)
line['title'] = line['filename'].split('.')[0]
if code == '':
datagroup.zip_file = new_zip_name
errors.append([count, "'document_type' field can't be empty"])
if DocumentType.objects.filter(group_type=datagroup.group_type, code=code
zf.close()
doc_type = DocumentType.objects.get(group_type=datagroup.group_type, code=code)
errors.append([count, "DocumentType code doesn't exist."])
datagroup.save()
filenames.append(line['filename'])
return redirect('data_group_detail', pk=datagroup.id)
doc = DataDocument(filename=line['filename'], title=line['title'],
    document_type=doc_type, url=line['url'], organization=line[
    'organization'], data_group=datagroup)
doc.save()
text.append(str(doc.pk) + ',' + ','.join(line.values()) + '\n')
