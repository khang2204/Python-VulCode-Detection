@login_required()...
datagroup = get_object_or_404(DataGroup, pk=pk)
if request.method == 'POST':
datagroup.delete()
return render(request, template_name, {'object': datagroup})
return redirect('data_group_list')
