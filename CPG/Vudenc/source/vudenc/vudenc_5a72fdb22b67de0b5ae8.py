@login_required()...
datagroup = get_object_or_404(DataGroup, pk=pk)
form = DataGroupForm(request.POST or None, instance=datagroup)
header = f'Update Data Group for Data Source "{datagroup.data_source}"'
if form.is_valid():
if form.has_changed():
form.referer = request.META.get('HTTP_REFERER', None)
form.save()
return redirect('data_group_detail', pk=datagroup.id)
if datagroup.extracted_docs():
form.fields['group_type'].disabled = True
groups = GroupType.objects.all()
for group in groups:
group.codes = DocumentType.objects.filter(group_type=group)
return render(request, template_name, {'datagroup': datagroup, 'form': form,
    'header': header, 'groups': groups})
