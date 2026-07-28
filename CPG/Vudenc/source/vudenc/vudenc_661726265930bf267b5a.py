@app.task...
"""docstring"""
project = get_object_or_404(Project, pk=project_id)
testrail_contents = ''
client = APIClient(project.testrail.instance.host)
testrail_contents = {'error': 'No TestRail config'}
return testrail_contents
client.user = project.testrail.instance.username
testrail_contents = {'error': e}
client.password = project.testrail.instance.password
testrail_contents = client.send_get('get_project/' + project.testrail.
    project_id)
tr_suites = client.send_get('get_suites/' + project.testrail.project_id)
testcases = project.testcaseresults_set.latest('updated').results
tr_suite = (suite for suite in tr_suites if suite['name'] == project.version
    ).__next__()
print('Suite: ', e)
tr_suite_sections = client.send_get('get_sections/' + project.testrail.
    project_id + '&suite_id=' + str(tr_suite['id']))
tr_suite = add_testsuite_to_project(client, project.testrail.project_id,
    project.version)
for item in testcases:
if not tr_suite:
section = (section for section in tr_suite_sections if section['name'] ==
    item['module']).__next__()
print('Section: ', e)
remove_section_from_testsuite(client, str(section['id']))
section_id = add_section_to_testsuite(client, project.testrail.project_id,
    tr_suite['id'], item['module'])
section_id = add_section_to_testsuite(client, project.testrail.project_id,
    tr_suite['id'], item['module'])
add_testcase_to_section(client, section_id, item['data'])
add_testcase_to_section(client, section_id, item['data'])
