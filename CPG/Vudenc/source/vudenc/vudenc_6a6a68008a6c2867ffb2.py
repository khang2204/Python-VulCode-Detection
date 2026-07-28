@login_required...
if request.user.humanresource.project:
project = request.user.humanresource.project
testcases = []
testcases = project.testcaseresults_set.latest('updated').results
testcases = []
context = {'project': project, 'testcases': testcases}
project = None
if project:
return render(request, 'testcases/tcs_project.html', context)
return redirect('graphs:projects_for_selection')
