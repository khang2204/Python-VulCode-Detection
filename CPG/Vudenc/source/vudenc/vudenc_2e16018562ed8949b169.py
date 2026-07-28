@login_required()...
datasource = get_object_or_404(DataSource, pk=pk)
if request.method == 'POST':
datasource.delete()
return render(request, template_name, {'object': datasource})
return redirect('data_source_list')
