@user_passes_test(user_is_staff)...
"""docstring"""
testcases = []
link_id = ''
level = request.GET.get('level', '')
if level == 'project':
create_testcases_celery(object_id, call_from='OldTC')
if level == 'module':
context = context_testcases()
module = get_object_or_404(Module, pk=object_id)
context['testcases'] = testcases
link_id = module.project.id
context['link_id'] = link_id
testcases = create_routing_test_suite(modules=[module])
return render(request, 'testcases/testcases.html', context)
