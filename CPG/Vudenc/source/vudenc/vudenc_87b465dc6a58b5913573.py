@user_passes_test(user_is_superuser)...
suites = []
testrail = get_object_or_404(TestRailConfiguration, pk=testrail_id)
client = APIClient(testrail.instance.host)
client.user = testrail.instance.username
client.password = testrail.instance.password
testrail_find_suites = client.send_get('get_suites/' + str(testrail.project_id)
    )
for suite in testrail_find_suites:
suites.append(suite['name'])
if testrail.test_suite != suites:
testrail.test_suite = suites
context = context_project_dashboard(request)
testrail.save()
context['last_tab'] = 'test_rails'
return render(request, 'projects/project_dashboard.html', context)
