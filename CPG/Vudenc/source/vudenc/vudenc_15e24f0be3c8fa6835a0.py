@login_required()...
datasource = get_object_or_404(DataSource, pk=pk)
docs = DataDocument.objects.filter(data_group__in=DataGroup.objects.filter(
    data_source=datasource))
datasource.registered = len(docs) / float(datasource.estimated_records) * 100
datasource.uploaded = len(docs.filter(matched=True)) / float(datasource.
    estimated_records) * 100
form = PriorityForm(request.POST or None, instance=datasource)
if request.method == 'POST':
if form.is_valid():
datagroup_list = DataGroup.objects.filter(data_source=pk)
priority = form.cleaned_data['priority']
context = {'object': datasource, 'datagroup_list': datagroup_list, 'form': form
    }
datasource.priority = priority
return render(request, template_name, context)
datasource.save()
