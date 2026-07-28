@login_required()...
datasources = DataSource.objects.all()
ds_list, frm_list = [], []
for ds in datasources:
frm_list.append(PriorityForm(request.POST or None, instance=ds))
registered = Count('datagroup__datadocument')
uploaded = Count('datagroup__datadocument', filter=Q(
    datagroup__datadocument__matched=True))
extracted = Count('datagroup__datadocument__extractedtext')
ds_list = DataSource.objects.annotate(registered=registered).annotate(uploaded
    =uploaded, extracted=extracted)
out = zip(ds_list, frm_list)
if request.method == 'POST':
datasource = DataSource.objects.get(pk=request.POST['ds_pk'])
return render(request, template_name, {'object_list': out})
form = PriorityForm(request.POST or None, instance=datasource)
if form.is_valid():
priority = form.cleaned_data['priority']
datasource.priority = priority
datasource.save()
return redirect('data_source_list')
