def get_feature(request, id):...
task = Project.objects.get(id=id)
if not task.has_perm(request.user, OI_READ):
return direct_to_template(request, template='funding/feature.html',
    extra_context={'object': task.master, 'task': task})
