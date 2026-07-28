@login_required()...
form = DataSourceForm(request.POST or None)
if form.is_valid():
form.save()
return render(request, template_name, {'form': form})
return redirect('data_source_list')
