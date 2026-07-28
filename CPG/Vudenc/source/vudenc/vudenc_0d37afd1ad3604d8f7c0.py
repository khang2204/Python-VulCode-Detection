@login_required...
"""docstring"""
level = request.GET.get('level', '')
if level == 'project':
project = get_object_or_404(Project, pk=object_id)
if level == 'module':
link_id = project.id
module = get_object_or_404(Module, pk=object_id)
testcases = []
testcases = project.testcaseresults_set.latest('updated').results
testcases = []
context = context_testcases()
link_id = module.project.id
link_id = ''
context['testcases'] = testcases
tmp_tcs = module.project.testcaseresults_set.latest('updated').results
testcases = []
context['link_id'] = link_id
testcases = [(item for item in tmp_tcs if item['module'] == module.name).
    __next__()]
return render(request, 'testcases/testcases.html', context)
