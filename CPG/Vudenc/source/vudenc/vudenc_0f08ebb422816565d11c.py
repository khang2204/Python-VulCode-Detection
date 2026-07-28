@login_required()...
datagroup = DataGroup.objects.all()
data = {}
data['object_list'] = datagroup
return render(request, template_name, data)
