@user_passes_test(user_is_staff)...
if request.method == 'GET':
context = {'form': TestrailConfigurationForm()}
if request.method == 'POST':
return render(request, 'testcases/tc_testrails_new.html', context)
instance = get_object_or_404(TestRailInstance, username='testrail@west.com')
testrail_projects = get_projects_from_testrail(instance)
form = TestrailConfigurationForm(request.POST)
if form.is_valid():
suites = []
messages.error(request, form.errors)
testrail_new = form.save(commit=False)
context = context_project_dashboard(request)
testrail_find = next(item for item in testrail_projects if item['name'] ==
    testrail_new.project_name)
context['last_tab'] = 'test_rails'
testrail_new.project_id = testrail_find['id']
return render(request, 'projects/project_dashboard.html', context)
client = APIClient(testrail_new.instance.host)
client.user = testrail_new.instance.username
client.password = testrail_new.instance.password
testrail_find_suites = client.send_get('get_suites/' + str(testrail_new.
    project_id))
for suite in testrail_find_suites:
suites.append(suite['name'])
testrail_new.test_suite = suites
testrail_new.save()
