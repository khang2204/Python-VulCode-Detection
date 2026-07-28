@login_required()...
datasource = get_object_or_404(DataSource, pk=pk)
form = DataSourceForm(request.POST or None, instance=datasource)
if form.is_valid():
if form.has_changed():
form.referer = request.META.get('HTTP_REFERER', None)
form.save()
return redirect('data_source_detail', pk=pk)
return render(request, template_name, {'form': form})
